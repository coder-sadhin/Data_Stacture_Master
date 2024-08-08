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


def test():
    "A set of unit tests."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units["C2"] == [
        ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2"],
        ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
        ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"],
    ]
    # fmt: off
    assert peers["C2"] == {
        "A2", "B2", "D2", "E2", "F2", "G2", "H2", "I2", "C1", "C3",
        "C4", "C5", "C6", "C7", "C8", "C9", "A1", "A3", "B1", "B3"
    }
    # fmt: on
    print("All tests pass.")


def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    ## To start, every square can be any digit; then assign values from the grid.
    values = {s: digits for s in squares}
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False  ## (Fail if we can't assign d to square s.)
    return values


def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in digits or c in "0."]
    assert len(chars) == 81
    return dict(zip(squares, chars))


def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, "")
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False



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
