from pathlib import Path

"""One-line time-machine warning label for a make.fun bounty."""

JOKE = "Draft: time-machine warning label pending final review."

OUTPUT_DIR = Path("/output")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")
