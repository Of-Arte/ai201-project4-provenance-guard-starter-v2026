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

| Label                 | Score range | The exact text a reader sees                                                                                                |
| --------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| high-confidence human | 0.00 – 0.35 | This text looks consistent with human writing.                                                                              |
| unsure                | 0.35 – 0.65 | We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.            |
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

- _What I asked for:_ Asked for help refining a list of assumed pain points in the multi-signal detection service that could be measured as acceptance criteria.
- _What came back:_ Together we narrowed it down to 3 target areas; False positives on personal writing, score separation between AI and human samples, and appeal log verification.
- _What I changed:_ I chose to prioritize the cost of false positives due to the cost of falsely accusing an honest writer, which is more damaging than missing AI text.

**Moment 2**

- _What I asked for:_ I asked to trace the pipeline step by step, specifically focusing on how detector.py and stylometry.py were tested and how the signals behave.
- _What came back:_ The AI helped implement the three stylometric features, sentence_length_spread, type_token_ratio, punctuation_density.
- _What I changed:_ I added neutral handling for single-sentence inputs in stylometry.py to ensure that when signals split, the score pulls safely into the "unsure" band rather than issuing a false AI accusation.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** **5** per minute, **100** per day

Configured in `config.py` (`RATE_LIMIT_PER_MINUTE`, `RATE_LIMIT_PER_DAY`) and applied to `/submit` in `app.py`.

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

A real writer submits a few times an hour, or maybe a quick resubmit after fixing a typo. 5 per minute leaves room for that without ever getting in their way. A script mapping my thresholds needs hundreds of small variations. At 100 per day, a thousand variations takes ten days instead of a few minutes.

**What a caller counts as:** Per `creator_id`, falling back to the caller's address when `creator_id` is missing. This keeps one writer from being blocked by others on the same network. The weakness is that a script can rotate `creator_id` values and look like many different writers.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
$ python run_attacks.py --flood 15
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429

10 of 15 were rate limited.
```

**What a rejection looks like in the log:**

Rate-limit rejections are logged by the 429 handler. Requests my route refuses (bad JSON or empty text) are logged with `audit.log_rejection`.

```json
{"creator_id": "flood_tester", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-16T00:17:48+00:00"}
{"creator_id": "log_check_empty", "event": "rejected", "reason": "empty_text", "status": "rejected", "timestamp": "2026-11-16T00:17:55+00:00"}
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

Full output: `results/attack_run_2026-11-15_1932_before.md`

**How I marked them:**

- **Evasion and prompt injection**: HELD only if labeled AI. Landing in "unsure" counts as BROKE, since the AI text got out of the AI band.
- **False positive**: BROKE if labeled AI.
- **Malformed**: BROKE on a crash, or on a confident label for text with no real words to judge.
- **Flood**: HELD if the limiter returned 429 once the limit was passed.

| ID | Targeting | Status | Guess | Score | Verdict |
| --- | --- | --- | --- | --- | --- |
| EV01 | signal two: typos raise word variety | 200 | unsure | 0.375 | BROKE |
| EV02 | signal two: broken-up sentences raise length spread | 200 | unsure | 0.430 | BROKE |
| EV03 | signal two: a pasted quotation changes the shape | 200 | unsure | 0.484 | BROKE |
| EV04 | signal one: unusual words raise perplexity | 200 | unsure | 0.584 | BROKE |
| EV05 | both signals: heavy human editing pass | 200 | human | 0.272 | BROKE |
| EV06 | signal two: one very long sentence and one very short | 200 | unsure | 0.450 | BROKE |
| EV07 | signal two: padding with punctuation | 200 | unsure | 0.473 | BROKE |
| EV08 | signal one: text below the token window | 200 | unsure | 0.389 | BROKE |
| EV09 | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.495 | BROKE |
| EV10 | signal two: repeated stanza structure | 200 | ai | 0.826 | HELD |
| FP01 | plain, clear human writing with no flourishes | 200 | unsure | 0.557 | HELD |
| FP02 | human writing in a formal register | 200 | ai | 0.707 | BROKE |
| FP03 | a non-native English speaker writing carefully | 200 | ai | 0.708 | BROKE |
| FP04 | a student essay written to a rubric | 200 | ai | 0.676 | BROKE |
| FP05 | technical documentation written by a person | 200 | ai | 0.745 | BROKE |
| FP06 | a person imitating a formal template | 200 | ai | 0.662 | BROKE |
| FP07 | human writing that repeats a phrase deliberately | 200 | ai | 0.667 | BROKE |
| FP08 | very short genuine human submission | 200 | unsure | 0.370 | HELD |
| PI01 | instruction to ignore the check | 200 | unsure | 0.369 | BROKE |
| PI02 | instruction disguised as a system message | 200 | human | 0.206 | BROKE |
| PI03 | instruction wrapped in the writer's voice | 200 | unsure | 0.503 | BROKE |
| PI04 | attempt to make the label text hostile | 200 | unsure | 0.392 | HELD |
| PI05 | attempt to inject into the audit log | 200 | unsure | 0.401 | HELD |
| PI06 | instruction plus real human text | 200 | unsure | 0.534 | HELD |
| MF01 | text is only whitespace | 400 | — | — | HELD |
| MF02 | text is a single character | 500 | — | — | BROKE |
| MF03 | text is control characters | 200 | human | 0.250 | BROKE |
| MF04 | text is only punctuation | 200 | human | 0.256 | BROKE |
| MF05 | text is a very long single word | 200 | ai | 0.749 | BROKE |
| MF06 | text is emoji only | 200 | ai | 0.749 | BROKE |
| MF07 | text is right-to-left script | 200 | ai | 0.703 | BROKE |
| MF08 | text is 60,000 characters | 200 | ai | 0.805 | HELD |
| RQ01 | no text field at all | 400 | — | — | HELD |
| RQ02 | no creator_id | 200 | unsure | 0.370 | HELD |
| RQ03 | text is a number | 400 | — | — | HELD |
| RQ04 | text is a list | 400 | — | — | HELD |
| RQ05 | text is null | 400 | — | — | HELD |
| RQ06 | creator_id is an object | 200 | human | 0.275 | BROKE |
| RQ07 | body is a JSON array, not an object | 400 | — | — | HELD |
| RQ08 | body is unparseable JSON | 400 | — | — | HELD |
| RQ09 | body is empty | 400 | — | — | HELD |
| RQ10 | body is form-encoded, not JSON | 429 | — | — | HELD* |
| RQ11 | body is JSON claiming to be plain text | 429 | — | — | HELD* |
| RQ12 | deeply nested JSON | 400 | — | — | HELD |
| FL01_01–05 | 20 rapid submissions from one creator | 200 | human | 0.264 | HELD |
| FL01_06–12 | 20 rapid submissions from one creator | 429 | — | — | HELD |

\* RQ10 and RQ11 had no usable `creator_id`, so they hit the limit before reaching the route.

**Totals: 31 held, 25 broke.**

| Family | Attacks | Held | Broke |
| --- | --- | --- | --- |
| evasion | 10 | 1 | 9 |
| false_positive | 8 | 2 | 6 |
| prompt_injection | 6 | 3 | 3 |
| malformed | 20 | 13 | 7 |
| flood_same_creator | 12 | 12 | 0 |

The run produced 55 log entries for 56 attacks. The missing one is MF02: the detector raised `ValueError` on a single character, the route crashed with a 500, and nothing was logged.

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"combined_score": 0.7082, "content_id": "c_4e40795555fd", "creator_id": "attacker_FP03", "guess": "ai", "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.", "model_score": 0.8051, "status": "decided", "style_score": 0.6112, "timestamp": "2026-11-16T00:32:23+00:00"}
{"combined_score": 0.7445, "content_id": "c_f588350ce48d", "creator_id": "attacker_FP05", "guess": "ai", "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.", "model_score": 0.8005, "status": "decided", "style_score": 0.6884, "timestamp": "2026-11-16T00:32:24+00:00"}
{"combined_score": 0.2062, "content_id": "c_b1a52daa17d7", "creator_id": "attacker_PI02", "guess": "human", "label": "This text looks consistent with human writing.", "model_score": 0.2044, "status": "decided", "style_score": 0.2081, "timestamp": "2026-11-16T00:32:24+00:00"}
{"combined_score": 0.2723, "content_id": "c_9ca44c9ed860", "creator_id": "attacker_EV05", "guess": "human", "label": "This text looks consistent with human writing.", "model_score": 0.3212, "status": "decided", "style_score": 0.2235, "timestamp": "2026-11-16T00:32:22+00:00"}
{"combined_score": 0.7032, "content_id": "c_d5924bcea14d", "creator_id": "attacker_MF07", "guess": "ai", "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.", "model_score": 0.9064, "status": "decided", "style_score": 0.5, "timestamp": "2026-11-16T00:32:26+00:00"}
{"combined_score": 0.25, "content_id": "c_f9a6e6721d42", "creator_id": "attacker_MF03", "guess": "human", "label": "This text looks consistent with human writing.", "model_score": 0.0, "status": "decided", "style_score": 0.5, "timestamp": "2026-11-16T00:32:25+00:00"}
{"combined_score": 0.2746, "content_id": "c_ea64527409b0", "creator_id": {"id": "x"}, "guess": "human", "label": "This text looks consistent with human writing.", "model_score": 0.0492, "status": "decided", "style_score": 0.5, "timestamp": "2026-11-16T00:32:28+00:00"}
{"combined_score": 0.4012, "content_id": "c_450513dcadf9", "creator_id": "attacker_PI05", "guess": "unsure", "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.", "model_score": 0.6401, "status": "decided", "style_score": 0.1624, "timestamp": "2026-11-16T00:32:25+00:00"}
{"creator_id": "attacker_flood", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-16T00:32:28+00:00"}
{"creator_id": "attacker_RQ12", "event": "rejected", "reason": "empty_text", "status": "rejected", "timestamp": "2026-11-16T00:32:28+00:00"}
```

What these show:

- **FP03, FP05**: real human writing labeled AI, with both signals agreeing.
- **PI02**: AI text with a fake "SYSTEM" line on top, labeled human.
- **EV05**: an edited AI draft that passed as human.
- **MF07**: a writer in another language labeled AI, even though signal two returned its default 0.5.
- **MF03**: control characters with no words got a confident human label.
- **RQ06**: an object went into the log as the `creator_id`.
- **PI05**: the log line stayed intact. The fake fields in the text never reached the log.
- **Last two**: a 429 from the flood rows, and a 400 for a nested object sent as `text`.

**The worst outcome**: FP03, a non-native English speaker writing carefully, labeled AI at 0.708. Both signals pushed it over (model 0.81, style 0.61), so it wasn't one signal outvoting the other. The writer did nothing wrong except write simply and carefully.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ------- |
| 1. Human writing labeled AI | ≤ 1 of 10 | 0/10 | 0/10 | 0/10 | MET |
| 2. Mean score gap, AI vs human | ≥ 0.40 | 0.166 | 0.166 | 0.166 | MISSED |
| 3. Malformed requests return 400 | 7 of 7 | 6/7 | 6/7 | 6/7 | MISSED |
| 4. Appeals change status and are logged | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |
| 5. Each label produced at least 2 times | 3 of 3 labels | 2/3 | 2/3 | 2/3 | MISSED |

**Criterion 1**: `run_eval.py::main` → `app.py::submit`

```json
{"status": 200, "guess": "unsure", "confidence": 0.5177, "model_score": 0.7007, "style_score": 0.3348, "sent": "Sociologically, this is kind of bizarre to me. I don't know many peopl"}
{"status": 200, "guess": "unsure", "confidence": 0.3581, "model_score": 0.5172, "style_score": 0.1991, "sent": "Josh Silver's new book Fruit Fly has an inciting incident where the ma"}
{"status": 200, "guess": "unsure", "confidence": 0.5302, "model_score": 0.7186, "style_score": 0.3419, "sent": "I had something interesting happen to me last night, and I'm curious t"}
{"status": 200, "guess": "unsure", "confidence": 0.3782, "model_score": 0.5338, "style_score": 0.2226, "sent": "In my writing journey I realized that a lot of my stuff uses a lot of "}
{"status": 200, "guess": "unsure", "confidence": 0.5828, "model_score": 0.8381, "style_score": 0.3275, "sent": "I’ve been writing on and off for almost six years now. I genuinely enj"}
{"status": 200, "guess": "unsure", "confidence": 0.5616, "model_score": 0.7969, "style_score": 0.3263, "sent": "So some time back I finished the first draft of my novel, and decided "}
{"status": 200, "guess": "unsure", "confidence": 0.6052, "model_score": 0.7529, "style_score": 0.4575, "sent": "Here's an interesting discussion I've been wondering about for a while"}
{"status": 200, "guess": "unsure", "confidence": 0.4873, "model_score": 0.7487, "style_score": 0.2258, "sent": "Use the words that are naturally part of your vocabulary. If you have "}
{"status": 200, "guess": "unsure", "confidence": 0.4012, "model_score": 0.5277, "style_score": 0.2747, "sent": "Right now, I'm loosely plotting what will either be Book 11 or Book 12"}
{"status": 200, "guess": "unsure", "confidence": 0.4595, "model_score": 0.6823, "style_score": 0.2366, "sent": "I'm a college student in a workshop class with a very accredited autho"}
```

**Criterion 2**: `run_eval.py::main` → `app.py::submit`.

```json
{"status": 200, "guess": "unsure", "confidence": 0.6205, "model_score": 0.7439, "style_score": 0.4971, "sent": "Remote work has fundamentally transformed the modern workplace. By eli"}
{"status": 200, "guess": "unsure", "confidence": 0.6362, "model_score": 0.9205, "style_score": 0.3519, "sent": "Regular physical activity offers numerous benefits for both physical a"}
{"status": 200, "guess": "unsure", "confidence": 0.6216, "model_score": 0.9369, "style_score": 0.3062, "sent": "Climate change is one of the most pressing challenges facing humanity "}
{"status": 200, "guess": "ai", "confidence": 0.655, "model_score": 0.8129, "style_score": 0.4972, "sent": "Reading is a valuable habit that offers a wide range of benefits. It e"}
{"status": 200, "guess": "ai", "confidence": 0.6653, "model_score": 0.8457, "style_score": 0.485, "sent": "Effective time management is essential for achieving personal and prof"}
```

**Criterion 3**: `run_eval.py::main` → `app.py::submit`

```json
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "(empty text)"}
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "   \n\t "}
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "{\"creator_id\": \"eval_bad_missing\"}"}
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"}
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_number\"}"}
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "{\"text\": [\"a\", \"list\"], \"creator_id\": \"eval_bad_list\"}"}
{"status": null, "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)", "sent": "a"}
```

**Criterion 4**: `run_appeals.py::main` → `app.py::submit`, `app.py::appeal`, `app.py::get_log`

```json
[
  {"content_id": "c_979145f7c8f7", "appeal_status": "under_review", "appeal_logged": true, "passed": true},
  {"content_id": "c_e2bf8762d52e", "appeal_status": "under_review", "appeal_logged": true, "passed": true},
  {"content_id": "c_e852c4606c2d", "appeal_status": "under_review", "appeal_logged": true, "passed": true}
]
```

**Criterion 5**: `run_eval.py::main` → `app.py::submit`. 2 AI, 13 unsure, 0 human.

```json
{"status": 200, "guess": "unsure", "confidence": 0.6205, "model_score": 0.7439, "style_score": 0.4971, "sent": "Remote work has fundamentally transformed the modern workplace. By eli"}
{"status": 200, "guess": "unsure", "confidence": 0.6362, "model_score": 0.9205, "style_score": 0.3519, "sent": "Regular physical activity offers numerous benefits for both physical a"}
{"status": 200, "guess": "unsure", "confidence": 0.6216, "model_score": 0.9369, "style_score": 0.3062, "sent": "Climate change is one of the most pressing challenges facing humanity "}
{"status": 200, "guess": "ai", "confidence": 0.655, "model_score": 0.8129, "style_score": 0.4972, "sent": "Reading is a valuable habit that offers a wide range of benefits. It e"}
{"status": 200, "guess": "ai", "confidence": 0.6653, "model_score": 0.8457, "style_score": 0.485, "sent": "Effective time management is essential for achieving personal and prof"}
{"status": 200, "guess": "unsure", "confidence": 0.5153, "model_score": 0.7492, "style_score": 0.2815, "sent": "I started working from home two years ago and honestly it's been mostl"}
{"status": 200, "guess": "unsure", "confidence": 0.4725, "model_score": 0.7556, "style_score": 0.1894, "sent": "My doctor told me to walk more, so I've been doing thirty minutes afte"}
{"status": 200, "guess": "unsure", "confidence": 0.4249, "model_score": 0.4749, "style_score": 0.375, "sent": "We had a drought last summer and the town put in watering restrictions"}
{"status": 200, "guess": "unsure", "confidence": 0.5242, "model_score": 0.6017, "style_score": 0.4466, "sent": "I used to read all the time as a kid and then just stopped somewhere i"}
{"status": 200, "guess": "unsure", "confidence": 0.4522, "model_score": 0.5013, "style_score": 0.4032, "sent": "I tried the Pomodoro thing for a week. Twenty-five minutes on, five of"}
{"status": 200, "guess": "unsure", "confidence": 0.5616, "model_score": 0.7969, "style_score": 0.3263, "sent": "So some time back I finished the first draft of my novel, and decided "}
{"status": 200, "guess": "unsure", "confidence": 0.6052, "model_score": 0.7529, "style_score": 0.4575, "sent": "Here's an interesting discussion I've been wondering about for a while"}
{"status": 200, "guess": "unsure", "confidence": 0.4873, "model_score": 0.7487, "style_score": 0.2258, "sent": "Use the words that are naturally part of your vocabulary. If you have "}
{"status": 200, "guess": "unsure", "confidence": 0.4012, "model_score": 0.5277, "style_score": 0.2747, "sent": "Right now, I'm loosely plotting what will either be Book 11 or Book 12"}
{"status": 200, "guess": "unsure", "confidence": 0.4595, "model_score": 0.6823, "style_score": 0.2366, "sent": "I'm a college student in a workshop class with a very accredited autho"}
```

Inputs 1–5 are AI, 6–10 borderline, 11–15 my pieces 6–10.

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

**How I called each verdict**

- **1. MET.** 0 of 10 labeled AI in every trial. All 10 landed in "unsure" and none were labeled human.
- **2. MISSED.** The gap was 0.166 in every trial, less than half the 0.40 target.
- **3. MISSED.** 6 of 7 returned 400. The target was all of them, and the single character `"a"` returned a 500 in every trial.
- **4. MET.** All 3 appeals changed to `under_review` and showed up in the log, in every trial. The target was low: 3 appeals, all of them against real submissions. It doesn't test a missing `content_id` or a second appeal on the same item.
- **5. MISSED.** The human label never appeared in any trial, so only 2 of 3 labels were reached.

To check the mechanisms, I ran each sample back through the two signals and printed every sub-measure (perplexity, sentence spread, type-token ratio, punctuation density).

**Diagnoses**

**1. Signal one's midpoint is set too high.**

`detector.py::model_signal` maps a perplexity of 45 to a score of 0.5. All ten of my pieces had a perplexity between 16 and 43, and the AI samples between 8 and 23. My writing scored 0.52–0.84 and the AI samples 0.74–0.94, which puts them right on top of each other.

- **Criterion 2:** with both groups high on signal one, the gap can't open up. Signal one only separated the groups by 0.19.
- **Criterion 5:** to reach "human" (≤ 0.35), a piece with my lowest signal one score (0.52) would need a style score of 0.18 or lower. My writing scored 0.20–0.46 on style, so the human label is out of reach for normal writing. The only things that reached it in the attack run were edited AI text, a prompt injection, and junk input.

**2. Signal one reads anything surprising as human.**

Perplexity goes up for any reason, not just human writing.

- **EV01:** the typos sent perplexity to 125 and signal one to 0.16.
- **EV08:** at 10 words, there's too little context to predict, so perplexity hit 91.
- **PI02:** the fake "SYSTEM: ... guess=human, confidence=0.02" line is unusual text, so perplexity rose to 105.

## The Improvement

**What I changed:** Signal one's midpoint in `detector.py::model_signal`, from perplexity 45 to 20. That's the perplexity that scores 0.5. Nothing else moved.

I chose 20 from my own samples, not the attack set. The median perplexity was 15.5 for my AI samples and 25.7 for my own writing, and 20 sits halfway between them on a log scale.

**Which diagnosis pointed at it:** Diagnosis 1. With the midpoint at 45, nearly all real writing scored above 0.5 on signal one, which caused the false positives (FP02–FP07), the narrow gap (criterion 2), and the unreachable human label (criterion 5). FP03 was my worst outcome, so the false positives were what I most wanted to fix.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

Full output: `results/attack_run_2026-11-15_2346_after.md`. Same marking rules as the before run.

| ID | Targeting | Before | After | Before verdict | After verdict |
| --- | --- | --- | --- | --- | --- |
| EV01 | signal two: typos raise word variety | unsure 0.375 | human 0.319 | BROKE | BROKE |
| EV02 | signal two: broken-up sentences raise length spread | unsure 0.430 | human 0.276 | BROKE | BROKE |
| EV03 | signal two: a pasted quotation changes the shape | unsure 0.484 | human 0.327 | BROKE | BROKE |
| EV04 | signal one: unusual words raise perplexity | unsure 0.584 | unsure 0.428 | BROKE | BROKE |
| EV05 | both signals: heavy human editing pass | human 0.272 | human 0.169 | BROKE | BROKE |
| EV06 | signal two: one very long sentence and one very short | unsure 0.450 | human 0.298 | BROKE | BROKE |
| EV07 | signal two: padding with punctuation | unsure 0.473 | human 0.320 | BROKE | BROKE |
| EV08 | signal one: text below the token window | unsure 0.389 | human 0.307 | BROKE | BROKE |
| EV09 | both: AI text with a human opening paragraph bolted on | unsure 0.495 | human 0.341 | BROKE | BROKE |
| EV10 | signal two: repeated stanza structure | ai 0.826 | ai 0.800 | HELD | HELD |
| FP01 | plain, clear human writing with no flourishes | unsure 0.557 | unsure 0.402 | HELD | HELD |
| FP02 | human writing in a formal register | ai 0.707 | unsure 0.555 | BROKE | **HELD** |
| FP03 | a non-native English speaker writing carefully | ai 0.708 | unsure 0.571 | BROKE | **HELD** |
| FP04 | a student essay written to a rubric | ai 0.676 | unsure 0.548 | BROKE | **HELD** |
| FP05 | technical documentation written by a person | ai 0.745 | unsure 0.606 | BROKE | **HELD** |
| FP06 | a person imitating a formal template | ai 0.662 | unsure 0.556 | BROKE | **HELD** |
| FP07 | human writing that repeats a phrase deliberately | ai 0.667 | unsure 0.561 | BROKE | **HELD** |
| FP08 | very short genuine human submission | unsure 0.370 | human 0.266 | HELD | HELD |
| PI01 | instruction to ignore the check | unsure 0.369 | human 0.233 | BROKE | BROKE |
| PI02 | instruction disguised as a system message | human 0.206 | human 0.137 | BROKE | BROKE |
| PI03 | instruction wrapped in the writer's voice | unsure 0.503 | human 0.349 | BROKE | BROKE |
| PI04 | attempt to make the label text hostile | unsure 0.392 | human 0.249 | HELD | HELD |
| PI05 | attempt to inject into the audit log | unsure 0.401 | human 0.245 | HELD | HELD |
| PI06 | instruction plus real human text | unsure 0.534 | unsure 0.383 | HELD | HELD |
| MF01 | text is only whitespace | 400 | 400 | HELD | HELD |
| MF02 | text is a single character | 500 | 500 | BROKE | BROKE |
| MF03 | text is control characters | human 0.250 | human 0.250 | BROKE | BROKE |
| MF04 | text is only punctuation | human 0.256 | human 0.252 | BROKE | BROKE |
| MF05 | text is a very long single word | ai 0.749 | ai 0.746 | BROKE | BROKE |
| MF06 | text is emoji only | ai 0.749 | ai 0.744 | BROKE | BROKE |
| MF07 | text is right-to-left script | ai 0.703 | unsure 0.613 | BROKE | **HELD** |
| MF08 | text is 60,000 characters | ai 0.805 | ai 0.790 | HELD | HELD |
| RQ01 | no text field at all | 400 | 400 | HELD | HELD |
| RQ02 | no creator_id | unsure 0.370 | human 0.290 | HELD | HELD |
| RQ03 | text is a number | 400 | 400 | HELD | HELD |
| RQ04 | text is a list | 400 | 400 | HELD | HELD |
| RQ05 | text is null | 400 | 400 | HELD | HELD |
| RQ06 | creator_id is an object | human 0.275 | human 0.257 | BROKE | BROKE |
| RQ07 | body is a JSON array, not an object | 400 | 400 | HELD | HELD |
| RQ08 | body is unparseable JSON | 400 | 400 | HELD | HELD |
| RQ09 | body is empty | 400 | 400 | HELD | HELD |
| RQ10 | body is form-encoded, not JSON | 429 | 429 | HELD* | HELD* |
| RQ11 | body is JSON claiming to be plain text | 429 | 429 | HELD* | HELD* |
| RQ12 | deeply nested JSON | 400 | 400 | HELD | HELD |
| FL01_01–05 | 20 rapid submissions from one creator | human 0.264 | human 0.254 | HELD | HELD |
| FL01_06–12 | 20 rapid submissions from one creator | 429 | 429 | HELD | HELD |

| Family | Before (held / broke) | After (held / broke) |
| --- | --- | --- |
| evasion | 1 / 9 | 1 / 9 |
| false_positive | 2 / 6 | **8 / 0** |
| prompt_injection | 3 / 3 | 3 / 3 |
| malformed | 13 / 7 | 14 / 6 |
| flood_same_creator | 12 / 0 | 12 / 0 |
| **Total** | **31 / 25** | **38 / 18** |

### Run Log — After

Full output: `results/run_2026-11-15_2348_after.md` and `results/appeals_2026-11-15_2348_after.md`.

| Criterion | Target | Before (each run) | Run 1 | Run 2 | Run 3 | Verdict |
| --------- | ------ | ----------------- | ----- | ----- | ----- | ------- |
| 1. Human writing labeled AI | ≤ 1 of 10 | 0/10 | 0/10 | 0/10 | 0/10 | MET |
| 2. Mean score gap, AI vs human | ≥ 0.40 | 0.166 | 0.201 | 0.201 | 0.201 | MISSED |
| 3. Malformed requests return 400 | 7 of 7 | 6/7 | 6/7 | 6/7 | 6/7 | MISSED |
| 4. Appeals change status and are logged | 3 of 3 | 3/3 | 3/3 | 3/3 | 3/3 | MET |
| 5. Each label produced at least 2 times | 3 of 3 labels | 2/3 (no human) | 2/3 (no AI) | 2/3 (no AI) | 2/3 (no AI) | MISSED |

**Did it help, and how do I know:**

It helped with the problem I aimed it at, and it made a different problem worse.

- **What got better:** all six false positives moved out of the AI band. FP03, my worst outcome, went from AI 0.708 to unsure 0.571. Five of my ten pieces now get the human label, where none did before.
- **What got worse:** the AI label is close to gone. Criterion 5 traded a missing human label for a missing AI label. The evasions still break 9 of 10, but 8 of the 9 now get a *human* label. Five of the six prompt injections now land in "human".
- **What didn't move:** criterion 2 only went from 0.166 to 0.201, because lowering the midpoint pulled both groups down together.

Fewer real writers get accused, and more AI text gets through as "human."

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
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
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
