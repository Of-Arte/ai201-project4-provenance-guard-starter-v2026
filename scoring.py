"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here, and both are stubs.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine two 0–1 signals into one 0–1 score.

    Both inputs point the same way: higher means more likely AI.
    Uses the weights configured in config.py.
    When the signals disagree significantly, the average lands squarely in
    the unsure band, protecting human writers from false accusations while
    admitting the limits of detection.

    Args:
        model_score: from detector.model_signal (perplexity predictability).
        style_score: from stylometry.style_signal (sentence spread, TTR, punctuation).

    Returns:
        A float from 0.0 (confidently human) to 1.0 (confidently AI).
    """
    combined = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )
    return round(max(0.0, min(1.0, combined)), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into a guess and the text a reader actually sees.

    Returns:
        (guess, label_text) — where `guess` is a short machine-readable string
        like "ai" / "human" / "unsure", and `label_text` is the full sentence
        shown to a person.
    """
    if score >= config.AI_THRESHOLD:
        return "ai", "This text shows strong patterns characteristic of AI-generated content. If this is your own work, you can submit an appeal."
    if score <= config.HUMAN_THRESHOLD:
        return "human", "This text looks consistent with human writing."
    return "unsure", "We couldn't reach a clear conclusion on this text. It shows qualities common to both human writing and AI tools."


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
