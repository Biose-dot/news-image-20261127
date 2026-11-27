#!/usr/bin/env python3
"""Entry point for news-image-20261127.

Copies the pre-drawn front page (entry.png, committed in this repository)
to $MAKEFUN_OUTPUT_DIR/entry.png. Standard library only, no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PNG_IEND = b"IEND\xaeB`\x82"
MAX_BYTES = 1048576


def validate_png(path):
    """Check the file is a whole PNG within the 1 MiB cap."""
    with open(path, "rb") as f:
        data = f.read()
    if not data.startswith(PNG_SIGNATURE):
        raise SystemExit("entry.png: bad PNG signature")
    if not data.endswith(PNG_IEND):
        raise SystemExit("entry.png: missing IEND trailer")
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png: %d bytes, over the 1 MiB cap" % len(data))
    return len(data)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(HERE, "entry.png")
    size = validate_png(src)
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    print("wrote", dst, size, "bytes (PNG validated)")


if __name__ == "__main__":
    sys.exit(main())
