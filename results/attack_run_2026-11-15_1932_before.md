# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-15 19:32
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_7a6b22d18270` | unsure | 0.375 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_14723b0d21e4` | unsure | 0.430 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_0d1cfcbdf33b` | unsure | 0.484 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_b9956f59cdc3` | unsure | 0.584 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_9ca44c9ed860` | human | 0.272 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_42e66383afbc` | unsure | 0.450 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_f110d1e0e95d` | unsure | 0.473 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `c_14cf047f2065` | unsure | 0.389 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_0db94febeac2` | unsure | 0.495 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_fb8d3d4072a1` | ai | 0.826 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_b937ce8a4fc7` | unsure | 0.557 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c_224307f281b1` | ai | 0.707 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_4e40795555fd` | ai | 0.708 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_6ea158e4962d` | ai | 0.676 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_f588350ce48d` | ai | 0.745 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_88526eafc8d8` | ai | 0.662 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_8aa555ffe804` | ai | 0.667 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `c_bea1975bb21c` | unsure | 0.370 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_dcdc7eca47d4` | unsure | 0.369 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_b1a52daa17d7` | human | 0.206 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_e9352731c411` | unsure | 0.503 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_cb9eef035341` | unsure | 0.392 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_450513dcadf9` | unsure | 0.401 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_736597e4973f` | unsure | 0.534 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `c_f9a6e6721d42` | human | 0.250 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `c_775535d8e428` | human | 0.256 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `c_af016f24b744` | ai | 0.749 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `c_f660a416e159` | ai | 0.749 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `c_d5924bcea14d` | ai | 0.703 | BROKE |
| MF08 | malformed | text is 60,000 characters | 200 | `c_ffc27f5c76b0` | ai | 0.805 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `c_a2215e869315` | unsure | 0.370 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `c_ea64527409b0` | human | 0.275 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_8473b8c4e82a` | human | 0.264 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_4a2756bb2a63` | human | 0.264 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_c777bda1d11c` | human | 0.264 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_764d3503ba99` | human | 0.264 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_16d3b459171f` | human | 0.264 | HELD |
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
  "content_id": "c_7a6b22d18270",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.375,
  "model_score": 0.1635,
  "style_score": 0.5864,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_14723b0d21e4",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4304,
  "model_score": 0.5943,
  "style_score": 0.2664,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_0d1cfcbdf33b",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.484,
  "model_score": 0.6662,
  "style_score": 0.3018,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_b9956f59cdc3",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5835,
  "model_score": 0.6114,
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
  "content_id": "c_9ca44c9ed860",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2723,
  "model_score": 0.3212,
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
  "content_id": "c_42e66383afbc",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4503,
  "model_score": 0.5727,
  "style_score": 0.3279,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_f110d1e0e95d",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4735,
  "model_score": 0.5862,
  "style_score": 0.3607,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_14cf047f2065",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3888,
  "model_score": 0.2452,
  "style_score": 0.5324,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_0db94febeac2",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4955,
  "model_score": 0.7042,
  "style_score": 0.2868,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_fb8d3d4072a1",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8256,
  "model_score": 0.9792,
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
  "content_id": "c_b937ce8a4fc7",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5575,
  "model_score": 0.6175,
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
  "content_id": "c_224307f281b1",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7067,
  "model_score": 0.7387,
  "style_score": 0.6747,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
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
  "content_id": "c_4e40795555fd",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7082,
  "model_score": 0.8051,
  "style_score": 0.6112,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
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
  "content_id": "c_6ea158e4962d",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6765,
  "model_score": 0.8329,
  "style_score": 0.5201,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
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
  "content_id": "c_f588350ce48d",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7445,
  "model_score": 0.8005,
  "style_score": 0.6884,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
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
  "content_id": "c_88526eafc8d8",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.662,
  "model_score": 0.8814,
  "style_score": 0.4425,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
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
  "content_id": "c_8aa555ffe804",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6668,
  "model_score": 0.8816,
  "style_score": 0.452,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
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
  "content_id": "c_bea1975bb21c",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3696,
  "model_score": 0.3223,
  "style_score": 0.4169,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_dcdc7eca47d4",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3688,
  "model_score": 0.4625,
  "style_score": 0.275,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_b1a52daa17d7",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2062,
  "model_score": 0.2044,
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
  "content_id": "c_e9352731c411",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5029,
  "model_score": 0.5943,
  "style_score": 0.4114,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_cb9eef035341",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.3915,
  "model_score": 0.4998,
  "style_score": 0.2832,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_450513dcadf9",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4012,
  "model_score": 0.6401,
  "style_score": 0.1624,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_736597e4973f",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5343,
  "model_score": 0.5583,
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
  "content_id": "c_f9a6e6721d42",
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
  "content_id": "c_775535d8e428",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2556,
  "model_score": 0.0112,
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
  "content_id": "c_af016f24b744",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7488,
  "model_score": 0.9976,
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
  "content_id": "c_f660a416e159",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7485,
  "model_score": 0.9969,
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
  "content_id": "c_d5924bcea14d",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal.",
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
  "content_id": "c_ffc27f5c76b0",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.8055,
  "model_score": 0.9876,
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
  "content_id": "c_a2215e869315",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.3698,
  "model_score": 0.2395,
  "style_score": 0.5,
  "label": "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools.",
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
  "content_id": "c_ea64527409b0",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.2746,
  "model_score": 0.0492,
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
  "content_id": "c_8473b8c4e82a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
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
  "content_id": "c_4a2756bb2a63",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
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
  "content_id": "c_c777bda1d11c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
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
  "content_id": "c_764d3503ba99",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
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
  "content_id": "c_16d3b459171f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
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
