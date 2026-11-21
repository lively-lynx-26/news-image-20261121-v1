"""Entry program for news-image-20261121.

The front page for Saturday 21 November 2026 was rendered in the build
session (diffusion hero panels + code-drawn text, PIL/DejaVu) and is
stored beside this file as entry.png. This program only copies that
image to the grader's output directory, then checks the copy is a
well-formed PNG of the expected size.

Usage: python3 main.py
Output: $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png)
"""

import hashlib
import os
import shutil
import sys

IMAGE_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SHA256 = "1a14979c7c6b176501a198ddfb4cbfd1ead9a957ea78596a3cbe52b13fc6ce2a"


def repo_root():
    return os.path.dirname(os.path.abspath(__file__))


def output_dir():
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(wanted, exist_ok=True)
        probe = os.path.join(wanted, ".write-test")
        with open(probe, "wb") as handle:
            handle.write(b"ok")
        os.remove(probe)
        return wanted
    except OSError:
        fallback = os.path.join(repo_root(), "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main():
    source = os.path.join(repo_root(), IMAGE_NAME)
    if not os.path.isfile(source):
        print("missing %s next to main.py" % IMAGE_NAME, file=sys.stderr)
        return 1
    dest_dir = output_dir()
    dest = os.path.join(dest_dir, IMAGE_NAME)
    shutil.copyfile(source, dest)
    with open(dest, "rb") as handle:
        data = handle.read()
    if data[:8] != PNG_MAGIC:
        print("output is not a PNG", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    try:
        from PIL import Image

        with Image.open(dest) as image:
            width, height = image.size
        if width > 1024 or height > 1024:
            print("output exceeds 1024x1024: %dx%d" % (width, height),
                  file=sys.stderr)
            return 1
        print("%s %dx%d %d bytes sha256 %s"
              % (dest, width, height, len(data), digest))
    except ImportError:
        print("%s %d bytes sha256 %s" % (dest, len(data), digest))
    if digest != EXPECTED_SHA256:
        print("WARNING: sha256 differs from the built image", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
