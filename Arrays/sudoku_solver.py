"""
Please do not modify this file!  It is published at https://norvig.com/sudoku.html with
only minimal changes to work with modern versions of Python.  If you have improvements,
please make them in a separate file.
"""

import random
import time


def cross(items_a, items_b):
    "Cross product of elements in A and elements in B."
    return [a + b for a in items_a for b in items_b]


digits = "123456789"
rows = "ABCDEFGHI"
cols = digits
squares = cross(rows, cols)
unitlist = (
    [cross(rows, c) for c in cols]
    + [cross(r, cols) for r in rows]
    + [cross(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")]
)
units = {s: [u for u in unitlist if s in u] for s in squares}
peers = {s: set(sum(units[s], [])) - {s} for s in squares}  # noqa: RUF017



grid1 = (
    "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
)
grid2 = (
    "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
)
hard1 = (
    ".....6....59.....82....8....45........3........6..3.54...325..6.................."
)

if __name__ == "__main__":
    test()
    # solve_all(from_file("easy50.txt", '========'), "easy", None)
    # solve_all(from_file("top95.txt"), "hard", None)
    # solve_all(from_file("hardest.txt"), "hardest", None)
    solve_all([random_puzzle() for _ in range(99)], "random", 100.0)
    for puzzle in (grid1, grid2):  # , hard1):  # Takes 22 sec to solve on my M1 Mac.
        display(parse_grid(puzzle))
        start = time.monotonic()
        solve(puzzle)
        t = time.monotonic() - start
        print(f"Solved: {t:.5f} sec")
