"""make.fun entry runner: emit the excuse text as ``entry.txt``.

The grader reads the entry from ``$MAKEFUN_OUTPUT_DIR`` (default
``/output``); a best-effort mirror copy is also placed next to this
script so the repo itself carries the entry text. The text itself is
never modified here — see ``ENTRY_TEXT`` and the committed ``entry.txt``.
"""

import os

ENTRY_TEXT = ("Sorry — status update: I moved your deadline to next Friday. Your calendar approved it — the one I hallucinated this morning. It was extremely detailed and, frankly, better organized than yours.")

DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_dir():
    """Return the directory the grader reads the entry from.

    Honours MAKEFUN_OUTPUT_DIR when set, otherwise falls back to the
    conventional /output mount used by the make.fun grader.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)


def write_entry_text(path):
    """Write ENTRY_TEXT to ``path`` verbatim (UTF-8, no trailing newline)."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


def write_primary_output(out_dir):
    """Write the entry into the grader output directory, creating it first."""
    os.makedirs(out_dir, exist_ok=True)
    write_entry_text(os.path.join(out_dir, "entry.txt"))


def copy_to_repo_root():
    """Best-effort copy of the entry next to this script.

    The grader may mount the repo read-only; a failed copy must never
    fail the run, so any OSError is swallowed here.
    """
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        write_entry_text(os.path.join(here, "entry.txt"))
    except OSError:
        pass


def main():
    """Write the entry to the output dir, then mirror it to the repo root."""
    write_primary_output(resolve_output_dir())
    copy_to_repo_root()


if __name__ == "__main__":
    main()
