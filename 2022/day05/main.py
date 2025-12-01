"""Day05 AOC."""

import re
import sys
from pathlib import Path


def Main(path: Path, part_num: int) -> None:
    """Day05 AOC."""
    cols: list[list[str]] = []
    for line in path.read_text().splitlines():
        if re.search(r"\[.\]", line):
            for idx in range(0, len(line), 4):
                box_col = (idx // 4) + 1
                box_val = line[idx + 1]
                if box_val.isalpha():
                    while len(cols) <= box_col:
                        cols.append([])
                    cols[box_col].insert(0, box_val)
        if match := re.match(r"move (\d+) from (\d+) to (\d+)", line):
            number_to_move = int(match.group(1))
            from_pile = int(match.group(2))
            to_pile = int(match.group(3))
            if part_num == 1:
                for _ in range(number_to_move):
                    value = cols[from_pile][-1]
                    cols[from_pile].pop()
                    cols[to_pile].append(value)
            else:
                value = cols[from_pile][-number_to_move:]
                cols[from_pile] = cols[from_pile][:-number_to_move]
                cols[to_pile] += value
    print(f"Pt {part_num} Final: ", end="")
    for c in cols[1:]:
        print(c[-1], end="")
    print()


if __name__ == "__main__":
    p = Path(sys.argv[1])
    Main(p, 1)
    Main(p, 2)
