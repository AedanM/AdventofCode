import sys
from pathlib import Path


def Part1(path: Path):
    directions: str = ""
    pos = (0, 0)
    houseDir: dict[tuple, int] = {}
    with path.open(mode="r") as fp:
        directions = fp.readline()
    for d in directions:
        houseDir[pos] = 1 if pos not in houseDir else houseDir[pos] + 1
        pos = CalcMovement(pos, d)

    return len(houseDir.keys())


def CalcMovement(pos, d):
    match d:
        case "v":
            pos = (pos[0], pos[1] - 1)
        case ">":
            pos = (pos[0] + 1, pos[1])
        case "<":
            pos = (pos[0] - 1, pos[1])
        case "^":
            pos = (pos[0], pos[1] + 1)
    return pos


def Part2(path: Path):
    directions: str = ""
    santaPos = (0, 0)
    robotPos = (0, 0)
    houseDir: dict[tuple, int] = {}
    with path.open(mode="r") as fp:
        directions = fp.readline()
    for idx, d in enumerate(directions):
        if idx % 2 == 0:
            houseDir[santaPos] = 1 if santaPos not in houseDir else houseDir[santaPos] + 1
            santaPos = CalcMovement(santaPos, d)
        else:
            houseDir[robotPos] = 1 if robotPos not in houseDir else houseDir[robotPos] + 1
            robotPos = CalcMovement(robotPos, d)
    return len(houseDir.keys())


if __name__ == "__main__":
    p = Path(sys.argv[1])
    print(Part1(p))
    print(Part2(p))
