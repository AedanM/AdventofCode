"""2015 Day25."""

# /// script
# dependencies = [
#     "tqdm",
# ]
# ///
from tqdm import tqdm


def GetIndexFromCoords(r: int, c: int) -> int:
    """O(1) index for triangle ordering (r,c) -> idx."""
    s = r + c - 1
    return (s - 1) * s // 2 + (s - r + 1)


def GetTriangleCoords(idx: int) -> tuple[int, int]:
    """O(1) inverse: idx -> (r, c)."""
    import math

    # s = smallest integer with s*(s+1)//2 >= idx
    s = int((math.sqrt(8 * idx + 1) - 1) // 2)
    if s * (s + 1) // 2 < idx:
        s += 1
    prev = s * (s - 1) // 2
    offset = idx - prev - 1
    return (s - offset, 1 + offset)


def Main(part_num: int) -> None:
    """2015 Day25."""
    coords = (2981, 3075)
    coords_count = (coords[0] + 1) * (coords[1] + 1) + 1
    max_x, max_y = GetTriangleCoords(coords_count)
    max_x *= 2
    max_y = max_x
    print("MAX", max_x, max_y, coords_count)
    grid = []
    [grid.append([0] * (2 * (max_y + 1))) for _ in range(2 * (max_x + 1))]

    print("Populating...")
    for idx in tqdm(range(1, coords_count + 1)):
        x, y = GetTriangleCoords(idx)
        grid[x][y] = idx

    for idx, x in enumerate(grid[1:]):
        if any(x):
            print(f"Row {idx}: ", end="")
            [print(f"{v:02d} ", end="") for v in x[1:] if v != 0]
            print()

    print(grid[coords[0]][coords[1]])


if __name__ == "__main__":
    Main(1)
