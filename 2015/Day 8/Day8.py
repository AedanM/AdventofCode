import re
import sys
from pathlib import Path


def Main(path: Path):
    lines = []
    with path.open() as fp:
        lines = fp.readlines()
    charCount = 0
    evalCount = 0
    escapeCount = 0
    for l in lines:
        startStr = l.replace("\n", "")
        charCount += len(startStr)
        evalCount += len(eval(startStr))
        escString = '"' + re.escape(startStr).replace('"', '\\"') + '"'
        escapeCount += len(escString)
    print(charCount - evalCount, escapeCount - charCount)


if __name__ == "__main__":
    p = Path(sys.argv[1])
    Main(p)
