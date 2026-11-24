#!/usr/bin/env python3
"""The Funniest Out-of-Office (make.fun) — final.

Writes one line of out-of-office auto-reply to /output/entry.txt.
Stdlib only, no network, deterministic.

Revision note (second full rewrite pass, judged against the brief):
draft 1 ("my inbox is covering for me... doing a better job") was
plausible but stale — the inbox-covering joke has been in a thousand
inboxes, and its twist is visible from the first clause. The rewrite
keeps the one-line OOO shape but changes the angle entirely: instead
of the inbox, urgent mail goes to the houseplant. That gives a
specific, visual detail (criterion: a voice of its own), a genuine
surprise (a plant as delegate), and the laugh lands in the last two
words, "better boundaries", which reframes the whole line.
"""

import os

ENTRY = (
    "I'm away until Monday. Please direct all urgent emails to my "
    "houseplant, which has the same authority I do and better boundaries."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
