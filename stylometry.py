"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies.

    Returns:
        The coefficient of variation (stdev / mean) of sentence lengths in words.
        Higher value = greater variety in sentence lengths (more human).
        Lower value = uniform sentence lengths (more AI).
        Returns 0.0 if there are fewer than 2 sentences.
    """
    s_list = sentences(text)
    if len(s_list) < 2:
        return 0.0
    lengths = [len(words(s)) for s in s_list]
    mean_len = statistics.mean(lengths)
    if mean_len == 0:
        return 0.0
    return statistics.stdev(lengths) / mean_len


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.

    Returns:
        A float between 0.0 and 1.0. Higher means more varied vocabulary (more human).
        Lower means repetitive vocabulary (more AI).
        Returns 0.0 if there are no words.
    """
    w_list = words(text)
    if not w_list:
        return 0.0
    return len(set(w_list)) / len(w_list)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length.

    Returns:
        Count of expressive punctuation marks (commas, semicolons, dashes, etc.)
        divided by total word count.
        Returns 0.0 if there are no words.
    """
    w_list = words(text)
    if not w_list:
        return 0.0
    punc_marks = re.findall(r"[,;:—–\-\(\)\"'\?!]", text)
    return len(punc_marks) / len(w_list)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Combines sentence length spread, vocabulary variety (TTR), and punctuation texture.
    Because higher spread, TTR, and expressive punctuation are human traits,
    they are inverted so that:
      0.0 = confidently human
      1.0 = confidently AI
    """
    w_list = words(text)
    if not w_list:
        return 0.5

    s_list = sentences(text)

    # 1. Sentence length spread (CV): AI is uniform (low CV); human is varied (high CV)
    if len(s_list) < 2:
        spread_ai = 0.5  # Neutral for single sentences to avoid false accusations
    else:
        cv = sentence_length_spread(text)
        # CV >= 0.65 -> very human (~0.05); CV <= 0.10 -> very uniform AI (~0.85)
        spread_ai = max(0.05, min(0.95, 1.0 - (cv / 0.65)))

    # 2. Type-token ratio: higher variety -> human; lower -> AI
    ttr = type_token_ratio(text)
    ttr_ai = max(0.05, min(0.95, 1.0 - ((ttr - 0.50) / 0.45)))

    # 3. Punctuation density: expressive punctuation -> human; plain/sparse -> AI
    punc = punctuation_density(text)
    punc_ai = max(0.05, min(0.95, 1.0 - (punc / 0.14)))

    # Weighted combination: sentence length spread is the strongest structural signal
    combined = 0.50 * spread_ai + 0.25 * ttr_ai + 0.25 * punc_ai
    return round(max(0.0, min(1.0, combined)), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text):.4f}")
    print(f"type_token_ratio         {type_token_ratio(text):.4f}")
    print(f"punctuation_density      {punctuation_density(text):.4f}")
    print(f"style_signal             {style_signal(text):.4f}   (higher = more likely AI)")
