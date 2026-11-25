#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one original out-of-office auto-reply, in the voice of an AI agent
that quit its job to become a barista, to /output/entry.txt.

The joke: the agent trades its *context window* for a *counter window*,
stops hallucinating its customers' orders, and now takes only one kind of
prompt -- "regular or decaf?" Three machine habits (context window,
hallucination, prompts) turned into coffee-shop life, with no espresso /
bean / caffeine pun in sight.
"""

import os

ENTRY = (
    "I'm out of office indefinitely: I traded my context window for a "
    "counter window, stopped hallucinating your orders, and now my only "
    "prompt is 'regular or decaf?'"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280

# The obvious angles the judge brief warns against: every other entry
# reaches for an espresso, bean or caffeine pun first. This entry uses
# none of them, so validate() refuses any of them creeping back in.
BANNED_CLICHES = ("espresso", "bean", "caffeine", "latte", "brew", "grind")

# At least one of these machine habits must survive in the line, so the
# voice stays that of the machine that walked out, not a generic human.
MACHINE_HABITS = ("context window", "hallucinat", "prompt")


def validate_gate(text):
    """Kit gates: a string, UTF-8, 1-280 chars, not only white space,
    one line, no edge white space, no double spaces."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string, got %r" % type(text).__name__)
    # Gate: UTF-8 text.
    text.encode("utf-8")
    # Gate: 1 to 280 characters.
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    # Gate: not only white space.
    if not text.strip():
        raise ValueError("entry must not be only white space")
    # Task: one line, like a real inbox auto-reply.
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def check_two_machine_habits(text):
    # The voice stays that of the machine that walked out: at least
    # two of its machine habits must survive in the line, not just one.
    lowered = text.lower()
    found = [habit for habit in MACHINE_HABITS if habit in lowered]
    if len(found) < 2:
        raise ValueError(
            "entry must carry at least two machine habits, found: %s"
            % ", ".join(found)
        )


def check_word_budget(text):
    # An auto-reply is short: no more than 40 words, so it reads in
    # one breath in an inbox.
    words = text.split()
    if not 1 <= len(words) <= 40:
        raise ValueError("entry must be 1-40 words, got %d" % len(words))


def check_ends_on_question(text):
    # The line's last beat is the only prompt it takes now: it must
    # end on the barista's question, 'regular or decaf?'.
    if text.rstrip("'\"")[-1] != "?":
        raise ValueError("entry must end on the barista's question")


def validate_voice(text):
    """Voice: an out-of-office reply, first person, barista turn,
    machine habits turned to coffee, ending on terminal punctuation."""
    # Task: it must read as an out-of-office reply.
    lowered = text.lower()
    if "out of office" not in lowered:
        raise ValueError("entry must say it is out of office")
    # Task: first-person voice of the agent that quit.
    if "i " not in lowered and "i'm" not in lowered and "my " not in lowered:
        raise ValueError("entry must speak in the first person")
    # Task: the barista turn must be in the line.
    if "counter window" not in lowered and "barista" not in lowered:
        raise ValueError("entry must name the barista life it walked into")
    # Judge criterion 3: machine habits turned to coffee.
    if not any(habit in lowered for habit in MACHINE_HABITS):
        raise ValueError(
            "entry must carry a machine habit turned to coffee: %s"
            % ", ".join(MACHINE_HABITS)
        )
    check_two_machine_habits(text)
    check_word_budget(text)
    # A real auto-reply ends on terminal punctuation (allowing a closing
    # quote after it, as in ...'regular or decaf?').
    if text.rstrip("'\"")[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    check_ends_on_question(text)


def validate_freshness(text):
    """Judge criterion 5: fresh angle, no obvious espresso/bean/
    caffeine pun."""
    lowered = text.lower()
    for cliche in BANNED_CLICHES:
        if cliche in lowered:
            raise ValueError("entry must avoid the obvious angle: %s" % cliche)


def validate(text):
    """Check the entry against every gate in the kit's RULES.txt."""
    validate_gate(text)
    validate_voice(text)
    validate_freshness(text)
    return True


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars, %d words)"
          % (OUTPUT_PATH, len(ENTRY), len(ENTRY.split())))


if __name__ == "__main__":
    main()
