"""3212. Count Submatrices With Equal Frequency of X and Y

Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:
grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:
Input: grid = [["X","Y","."],["Y",".","."]]
Output: 3

Example 2:
Input: grid = [["X","X"],["X","Y"]]
Output: 0

for Explaination see the question on  leetcode and see the image that are explaining well

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'."""

from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        prefix_x = [[0] * n for _ in range(m)]
        prefix_y = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                px = 1 if grid[i][j] == 'X' else 0
                py = 1 if grid[i][j] == 'Y' else 0

                if i > 0:
                    px += prefix_x[i-1][j]
                    py += prefix_y[i-1][j]
                if j > 0:
                    px += prefix_x[i][j-1]
                    py += prefix_y[i][j-1]
                if i > 0 and j > 0:
                    px -= prefix_x[i-1][j-1]
                    py -= prefix_y[i-1][j-1]

                prefix_x[i][j] = px
                prefix_y[i][j] = py

        count = 0
        for i in range(m):
            for j in range(n):
                x = prefix_x[i][j]
                y = prefix_y[i][j]
                if x == y and x > 0:
                    count += 1

        return count


# ── Test Runner

def run_tests():
    sol = Solution()

    tests = [
        (
            [["X","Y",".","."],["Y",".",".","."]],
            3,
            "Example 1"
        ),
        (
            [["X","X"],["X","Y"]],
            0,
            "Example 2 — no equal frequency"
        ),
        (
            [[".",".","."],[".",".",".",]],
            0,
            "Example 3 — no X at all"
        ),
        (
            [["X"]],
            0,
            "Single X, no Y"
        ),
        (
            [["X","Y"]],
            1,
            "Single row X,Y"
        ),
        (
            [["X","Y","X","Y"]],
            2,
            "Row: X Y X Y"
        ),
        (
            [["X","Y"],["Y","X"]],
            2,
            "2x2 symmetric grid"
        ),
    ]

    passed = 0
    failed = 0

    print("=" * 55)
    print("  LeetCode 3212 — Submatrices With Equal Freq X & Y")
    print("=" * 55)

    for i, (grid, expected, desc) in enumerate(tests, 1):
        result = sol.numberOfSubmatrices(grid)
        status = "PASS ✓" if result == expected else "FAIL ✗"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"  Test {i}: {status} | {desc}")
        if result != expected:
            print(f"           Expected {expected}, got {result}")

    print("=" * 55)
    print(f"  Results: {passed} passed, {failed} failed")
    print("=" * 55)


if __name__ == "__main__":
    run_tests()