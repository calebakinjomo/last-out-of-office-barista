#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply, in the voice of an AI agent that
quit its job to become a barista, to /output/entry.txt.

Judge criteria: it must read like a real inbox auto-reply, turn the
agent's machine habits (context window, answering messages) into coffee
(barista, one cup, pouring), and stay funny cold. The entry is capped
at 280 characters; this one is 150.
"""

import os

ENTRY = (
    "Thank you for your email. I have left this inbox to become a barista "
    "\u2014 my context window is now one cup, and I no longer answer "
    "messages, I just pour."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
