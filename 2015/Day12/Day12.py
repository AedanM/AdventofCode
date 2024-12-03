import re
import sys
from pathlib import Path


def Main(path: Path):
    sumTotal = 0
    strCount = ""
    for i in path.open().read():
        if i.isnumeric():
            strCount += i
        elif strCount != "":
            sumTotal += int(strCount)
            strCount = ""
    for i in re.findall(r"-\d+", path.open().read()):
        sumTotal += int(i)
    return sumTotal


def Main2(path: Path):
    sumTotal = 0
    text = path.read_text()
    for match in re.finditer(r"(-)?\d+", text):
        sumTotal += int(match.group())

    p2Total = sumTotal
    for match in re.finditer(r":\"red\"", path.read_text()):
        start = list(re.finditer(r"\{", text[: match.start()]))[-1].start()
        end = list(re.finditer(r"\}", text[match.start() :]))[0].end() + match.start()
        for match in re.finditer(r"(-)?\d+", text[start:end]):
            p2Total -= int(match.group())
    return sumTotal, p2Total


if __name__ == "__main__":
    p = Path(sys.argv[1])
    print(Main2(p))
