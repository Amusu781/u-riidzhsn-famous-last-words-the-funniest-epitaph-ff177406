#!/usr/bin/env python3
"""Write one epitaph line to /output/entry.txt."""

import os
import shutil

EPITAPH = "I finally won an argument with my wife. It only took dying to do it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Clear only the contents of /output, never /output itself.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()
