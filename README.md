# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. **Request Ingestion (`POST /submit`)**: A client sends a JSON payload containing raw `text` and `creator_id` to the web service, which validates invalid JSON and empty text.
2. **Signal 1 Evaluation (`detector.py`)**: The text is evaluated by gpt2 to evaluate token predictability, then converted into a score between 0.0 and 1.0.
3. **Signal 2 Evaluation (`stylometry.py`)**: The text is evaluated for sentence length variation, type-token vocabulary ratio, punctuation density without semantic reading, generating a style score between 0.0 and 1.0.
4. **Signal Scoring (`scoring.py`)**: The two independent signal scores are combined using defined weighting/disagreement rules into an overall confidence score and a categorical classification (`guess`).
5. **Label Generation (`scoring.py`)**: The numerical score is mapped into a label string for human readers and writers.
6. **Audit Logging (`audit.py`)**: A unique `content_id` is generated, and an audit record with timestamp, creator ID, signal scores, final score, and status (`decided`) is appended to `logs/audit.jsonl`.
7. **Response Delivery (`POST /appeal`)**: The service returns JSON with the `content_id`, guess, confidence, label, and both signal scores. If a writer disputes a false positive, they can submit an appeal referencing the `content_id` to flag the submission as `under_review`.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
Token predictability evaluated by gpt2. It measures how predictable each next token is given preceding context, then produces a score from 0.0 to 1.0.

**Why that might differ between human and AI writing:**
Language models generate text by predicting next tokens. Human writing has more variation with unique word choices and sentence structure.

**What it can't see:**
It only measures how predictable words are. It can't tell if the text is meaningful or not. Common words are easy to predict. Writing with unusual words can trick the model into thinking it is human.

### Signal two — the style signal

**What it measures:**
Structural metrics of raw text without semantic comprehension (sentence length variation, vocabulary diversity, and punctuation density).

**Why that might differ between human and AI writing:**
AI models default toward balanced sentence lengths and a consistent vocabulary across paragraphs. Human writing exhibits natural variation and distinct punctuation habits.

**What it can't see:**
It cannot read or understand meaning. Changes to the text layout or structure without altering content will fool or swing the stylometric evaluation.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
A balanced weighted average of the model predictability signal and the stylometric signal. When the two signals disagree, the combined score settles toward the middle "unsure" band (`0.35` to `0.65`). This captures uncertainty rather than forcing a high-confidence verdict.

**The numbers:**
`combined_score = (0.50 * model_score) + (0.50 * style_score)`
Configured in `config.py`:

- `WEIGHT_MODEL_SIGNAL = 0.50`
- `WEIGHT_STYLE_SIGNAL = 0.50`
- `HUMAN_THRESHOLD = 0.35` (scores `<= 0.35` $\rightarrow$ high-confidence human)
- `AI_THRESHOLD = 0.65` (scores `>= 0.65` $\rightarrow$ high-confidence AI)

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
In conventional human writing, the model signal flags the text as highly AI-like because ordinary words in simple sentences are very easy for GPT-2 to predict. However, the stylometric signal recognizes sentence length variability and human cadence, scoring much lower. The combining rule balances both to produce a score in the `0.55 - 0.60` range, placing it safely in the "unsure" band and preventing a false accusation.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label                 | Score range | The exact text a reader sees |
| --------------------- | ----------- | ---------------------------- |
| high-confidence human | 0.00 – 0.35 | This text looks consistent with human writing. |
| unsure                | 0.35 – 0.65 | We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools. |
| high-confidence AI    | 0.65 – 1.00 | This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal. |

**Why I worded the "unsure" one this way:**
The "unsure" label deliberately frames the result as a limitation of our automated system rather than an accusation against the author. It avoids alarming words like "flagged" or "suspicious," which alienate honest human writers whose style happens to fall near common language patterns. By stating that mixed qualities are natural and no definitive conclusion was reached, it sets clear expectations without hostility.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "In recent years, the integration of artificial intelligence into educational settings has gained significant momentum. Educational institutions are increasingly exploring ways to enhance learning experiences through intelligent tutoring systems.", "creator_id": "student_01"}'
```

```json
{
  "combined_score": 0.6861,
  "confidence": 0.6861,
  "content_id": "c_e43bc76383f4",
  "creator_id": "student_01",
  "guess": "ai",
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
  "model_score": 0.6908,
  "style_score": 0.6814
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "c_e43bc76383f4", "reasoning": "This essay was researched and drafted independently for my education class."}'
```

```json
{
  "content_id": "c_e43bc76383f4",
  "message": "Appeal recorded. Your submission is now under review.",
  "ok": true,
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.6861,
      "content_id": "c_e43bc76383f4",
      "creator_id": "student_01",
      "guess": "ai",
      "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
      "model_score": 0.6908,
      "status": "decided",
      "style_score": 0.6814,
      "timestamp": "2026-11-06T18:47:40+00:00"
    },
    {
      "content_id": "c_e43bc76383f4",
      "creator_id": "student_01",
      "event": "appeal",
      "reasoning": "This essay was researched and drafted independently for my education class.",
      "status": "under_review",
      "timestamp": "2026-11-06T18:47:40+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- _What I asked for:_
- _What came back:_
- _What I changed:_

**Moment 2**

- _What I asked for:_
- _What came back:_
- _What I changed:_

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** **_ per minute, _** per day

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ------- |
| 1.        |        |       |       |       |         |
| 2.        |        |       |       |       |         |
| 3.        |        |       |       |       |         |
| 4.        |        |       |       |       |         |
| 5.        |        |       |       |       |         |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
