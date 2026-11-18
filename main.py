"""Copy the pre-rendered front page to the output directory.

Standard library only: the grading server installs nothing, so this program
uses only os, shutil, sys and pathlib. The finished entry.png is committed
in this repo; the program just copies it to MAKEFUN_OUTPUT_DIR (or /output).
"""
import os
import shutil
import sys
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if not src.is_file():
        print("entry.png missing", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = Path(out_dir) / "entry.png"
    shutil.copyfile(src, dst)
    if dst.stat().st_size != src.stat().st_size:
        print("size mismatch after copy", file=sys.stderr)
        sys.exit(1)
    print(f"copied entry.png ({src.stat().st_size} bytes) to {dst}")


if __name__ == "__main__":
    main()
