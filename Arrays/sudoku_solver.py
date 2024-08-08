"""
Please do not modify this file!  It is published at https://norvig.com/sudoku.html with
only minimal changes to work with modern versions of Python.  If you have improvements,
please make them in a separate file.
"""

import random
import time



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
