import sys
from pathlib import Path


def Main(path: Path, part_num: int):
    marker_len = 4 if part_num == 1 else 14
    for line in path.read_text().splitlines():
        for idx in range(len(line)):
            markers = line[idx : idx + marker_len]
            if len(set(markers)) == marker_len:
                print(f"Part {part_num}: {idx + marker_len}")
                break


if __name__ == "__main__":
    p = Path(sys.argv[1])
    Main(p, 1)
    Main(p, 2)
