import sys
from pathlib import Path
from pprint import pp


def Main(path: Path):
    lines = []
    with path.open() as fp:
        lines = fp.readlines()

    routes = []
    for line in lines:
        splitLine = line.replace("\n", "").split(" ")
        routes.append((splitLine[0], splitLine[2], splitLine[-1]))
    routes = sorted(routes, key=lambda x: int(x[2]))
    locations = list(set(sorted([x[0] for x in routes] + [x[1] for x in routes])))
    visited = []
    used = []
    for r in routes:
        d1, d2, rLen = r
        if visited.count(d1) < 2 and visited.count(d2) < 2:
            visited += [d1, d2]
            used.append(r)
    print(f"Min {sum(int(x[2]) for x in used[:-1])}")

    visited = []
    used = []
    routes = sorted(routes, key=lambda x: int(x[2]), reverse=True)

    for r in routes:
        d1, d2, _rLen = r
        if visited.count(d1) < 2 and visited.count(d2) < 2 and _rLen != '99':
            visited += [d1, d2]
            used.append(r)
    pp(used)
    print(f"Max {sum(int(x[2]) for x in used)}")


if __name__ == "__main__":
    p = Path(sys.argv[1])
    Main(p)
