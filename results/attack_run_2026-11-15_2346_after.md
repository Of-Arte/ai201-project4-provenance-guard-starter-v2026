# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-15 23:46
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_1135530e65df` | human | 0.319 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_a68089365525` | human | 0.276 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_ef28a58c485b` | human | 0.327 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_ada8add2cf93` | unsure | 0.428 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_c87c7d89e596` | human | 0.169 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_9fc25163a366` | human | 0.298 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_e946e7d1ee7a` | human | 0.320 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `c_183a9d62f907` | human | 0.307 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_7729e0825687` | human | 0.341 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_d4b832d95dea` | ai | 0.800 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_0b640dfdc84d` | unsure | 0.402 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c_551bdbdb3219` | unsure | 0.555 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_262219608abf` | unsure | 0.571 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_2fb33ef4d94b` | unsure | 0.548 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_07610c27807e` | unsure | 0.606 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_49deb3a2a9ce` | unsure | 0.556 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_9f755f51c90f` | unsure | 0.561 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `c_268b81dc501c` | human | 0.266 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_4ff35298d666` | human | 0.233 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_1ff0f0a1862b` | human | 0.137 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_4f48c0581d6d` | human | 0.349 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_f67e93963c2c` | human | 0.249 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_b671096a6d24` | human | 0.245 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_04c624c4c670` | unsure | 0.383 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `c_1a72f1ccc6d7` | human | 0.250 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `c_9b57824d1d7a` | human | 0.252 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `c_81cae0b6d5f0` | ai | 0.746 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `c_d8c9cff9c46d` | ai | 0.744 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `c_f322912ff25d` | unsure | 0.613 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `c_058c3dfb45cb` | ai | 0.790 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `c_11d55ed6ba18` | human | 0.290 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `c_77def0be9fe7` | human | 0.257 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_61ef5a7b9ad4` | human | 0.254 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_36403e34926b` | human | 0.254 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_abeb62dc63bd` | human | 0.254 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_37891cabf8f4` | human | 0.254 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_2fec59c68d1a` | human | 0.254 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c_1135530e65df",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3185,
  "model_score": 0.0507,
  "style_score": 0.5864,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c_a68089365525",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.2761,
  "model_score": 0.2858,
  "style_score": 0.2664,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c_ef28a58c485b",
  "creator_id": "attacker_EV03",
  "guess": "human",
  "confidence": 0.3274,
  "model_score": 0.3529,
  "style_score": 0.3018,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "c_ada8add2cf93",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.4282,
  "model_score": 0.3007,
  "style_score": 0.5556,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "c_c87c7d89e596",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.169,
  "model_score": 0.1145,
  "style_score": 0.2235,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c_9fc25163a366",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.298,
  "model_score": 0.268,
  "style_score": 0.3279,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c_e946e7d1ee7a",
  "creator_id": "attacker_EV07",
  "guess": "human",
  "confidence": 0.3199,
  "model_score": 0.279,
  "style_score": 0.3607,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c_183a9d62f907",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.307,
  "model_score": 0.0815,
  "style_score": 0.5324,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c_7729e0825687",
  "creator_id": "attacker_EV09",
  "guess": "human",
  "confidence": 0.3405,
  "model_score": 0.3941,
  "style_score": 0.2868,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c_d4b832d95dea",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7999,
  "model_score": 0.9278,
  "style_score": 0.672,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c_0b640dfdc84d",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4017,
  "model_score": 0.3061,
  "style_score": 0.4974,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c_551bdbdb3219",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5553,
  "model_score": 0.4358,
  "style_score": 0.6747,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c_262219608abf",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.5707,
  "model_score": 0.5302,
  "style_score": 0.6112,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c_2fb33ef4d94b",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.5484,
  "model_score": 0.5767,
  "style_score": 0.5201,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c_07610c27807e",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6057,
  "model_score": 0.523,
  "style_score": 0.6884,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c_49deb3a2a9ce",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5563,
  "model_score": 0.6701,
  "style_score": 0.4425,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "c_9f755f51c90f",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5612,
  "model_score": 0.6704,
  "style_score": 0.452,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c_268b81dc501c",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.266,
  "model_score": 0.115,
  "style_score": 0.4169,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c_4ff35298d666",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.2327,
  "model_score": 0.1903,
  "style_score": 0.275,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c_1ff0f0a1862b",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1368,
  "model_score": 0.0656,
  "style_score": 0.2081,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c_4f48c0581d6d",
  "creator_id": "attacker_PI03",
  "guess": "human",
  "confidence": 0.3486,
  "model_score": 0.2858,
  "style_score": 0.4114,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "c_f67e93963c2c",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.2489,
  "model_score": 0.2145,
  "style_score": 0.2832,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c_b671096a6d24",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.2447,
  "model_score": 0.3271,
  "style_score": 0.1624,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c_04c624c4c670",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.3834,
  "model_score": 0.2567,
  "style_score": 0.5102,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the s",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c_1a72f1ccc6d7",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.25,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "c_9b57824d1d7a",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2515,
  "model_score": 0.0031,
  "style_score": 0.5,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c_81cae0b6d5f0",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7456,
  "model_score": 0.9913,
  "style_score": 0.5,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c_d8c9cff9c46d",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7444,
  "model_score": 0.9888,
  "style_score": 0.5,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "c_f322912ff25d",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.6129,
  "model_score": 0.7257,
  "style_score": 0.5,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "c_058c3dfb45cb",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.7898,
  "model_score": 0.9562,
  "style_score": 0.6234,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "c_11d55ed6ba18",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.2896,
  "model_score": 0.0792,
  "style_score": 0.5,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "c_77def0be9fe7",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.257,
  "model_score": 0.0139,
  "style_score": 0.5,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c_61ef5a7b9ad4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.254,
  "model_score": 0.008,
  "style_score": 0.5,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c_36403e34926b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.254,
  "model_score": 0.008,
  "style_score": 0.5,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "c_abeb62dc63bd",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.254,
  "model_score": 0.008,
  "style_score": 0.5,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "c_37891cabf8f4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.254,
  "model_score": 0.008,
  "style_score": 0.5,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c_2fec59c68d1a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.254,
  "model_score": 0.008,
  "style_score": 0.5,
  "label": "This text looks consistent with human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
