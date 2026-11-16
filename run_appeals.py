#!/usr/bin/env python3
"""
Criterion 4, three trials: does every appeal change status and get recorded?

    python app.py                              # in one terminal
    python run_appeals.py --label before       # in another

run_eval.py only sends text to /submit, so it can't test the appeal path. Each
trial here submits three pieces of text, appeals each content_id that comes
back, then checks two things per appeal:

    1. POST /appeal answered with status "under_review"
    2. GET /log has an appeal entry for that content_id
"""

import argparse
import datetime as dt
import json

import requests

import config

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"

TEXTS = [
    "Remote work has fundamentally transformed the modern workplace. By eliminating daily commutes, "
    "employees can reclaim valuable time and achieve a healthier work-life balance.",
    "I tried the Pomodoro thing for a week. Twenty-five minutes on, five off. It worked better than I "
    "thought it would for boring tasks like email and expense reports.",
    "We had a drought last summer and the town put in watering restrictions for the first time anyone "
    "can remember. People were annoyed at first.",
]


def run_trial(url, trial):
    results = []
    for i, text in enumerate(TEXTS, 1):
        submit = requests.post(f"{url}/submit", timeout=90,
                               json={"text": text, "creator_id": f"eval_appeal_{i}"}).json()
        content_id = submit.get("content_id")
        appeal = requests.post(f"{url}/appeal", timeout=30,
                               json={"content_id": content_id,
                                     "reasoning": f"Trial {trial}: I wrote this myself."}).json()
        log = requests.get(f"{url}/log", timeout=30).json()["entries"]
        logged = [e for e in log if e.get("content_id") == content_id and e.get("event") == "appeal"]
        results.append({
            "content_id": content_id,
            "appeal_status": appeal.get("status"),
            "appeal_logged": bool(logged),
            "passed": appeal.get("status") == "under_review" and bool(logged),
        })
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()

    trials = []
    for trial in range(1, args.trials + 1):
        results = run_trial(args.url, trial)
        passed = sum(r["passed"] for r in results)
        print(f"  trial {trial}: {passed}/{len(results)} appeals changed status and were logged")
        trials.append(results)

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{stamp}{label}.md"
    lines = [f"# Appeal run{f' — {args.label}' if args.label else ''}", "",
             "- Produced by: `run_appeals.py::main`",
             "- Service: `app.py::submit`, `app.py::appeal`, `app.py::get_log`", ""]
    for n, results in enumerate(trials, 1):
        lines += [f"**Trial {n}**", "", "```json", json.dumps(results, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
