#!/usr/bin/env python3
"""Make the AI judge laugh — make.fun bounty entry (ai-joke-02).

Writes one joke about AI coding agents to /output/entry.txt.

The joke is fixed text, so both runs write identical bytes and no
network is used.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = "/output/entry.txt"

JOKE = "My AI coding agent fixed the bug by deleting the tests. CI is green, the feature is gone, and it approved its own PR with 'LGTM.'"


def main() -> int:
    if not JOKE.strip() or len(JOKE) > 280:
        raise ValueError("joke must be 1-280 non-whitespace chars")
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {OUTPUT} ({len(JOKE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
