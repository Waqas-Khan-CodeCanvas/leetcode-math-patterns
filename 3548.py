"""
3548. Equal Sum Grid Partition II
    You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
    Each of the two resulting sections formed by the cut is non-empty.
    The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
    If a cell is discounted, the rest of the section must remain connected.
    Return true if such a partition exists; otherwise, return false.

Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

Example 1:
Input: grid = [[1,4],[2,3]]
Output: true
Explanation:
A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.


Example 2:
Input: grid = [[1,2],[3,4]]
Output: true
Explanation:
A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.


Example 3:
Input: grid = [[1,2,4],[2,3,5]]
Output: false
Explanation:
A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.


Example 4:
Input: grid = [[4,1,8],[3,2,6]]
Output: false
Explanation:
No valid cut exists, so the answer is false.

"""

from typing import List
from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        # ---------- Horizontal cuts ----------
        top_sum = 0
        bottom_counter = Counter()
        for row in grid:
            bottom_counter.update(row)

        top_counter = Counter()

        for i in range(m - 1):
            for val in grid[i]:
                top_counter[val] += 1
                bottom_counter[val] -= 1
                if bottom_counter[val] == 0:
                    del bottom_counter[val]

            top_sum += sum(grid[i])
            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            if top_sum > bottom_sum:
                if self.can_remove(grid, 0, i, 0, n - 1, diff, top_counter, i + 1, n):
                    return True
            else:
                if self.can_remove(grid, i + 1, m - 1, 0, n - 1, diff, bottom_counter, m - (i + 1), n):
                    return True

        # ---------- Vertical cuts ----------
        left_sum = 0
        right_counter = Counter()
        for j in range(n):
            for i in range(m):
                right_counter[grid[i][j]] += 1

        left_counter = Counter()

        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                left_counter[val] += 1
                right_counter[val] -= 1
                if right_counter[val] == 0:
                    del right_counter[val]

            left_sum += sum(grid[i][j] for i in range(m))
            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            if left_sum > right_sum:
                if self.can_remove(grid, 0, m - 1, 0, j, diff, left_counter, m, j + 1):
                    return True
            else:
                if self.can_remove(grid, 0, m - 1, j + 1, n - 1, diff, right_counter, m, n - (j + 1)):
                    return True

        return False

    def can_remove(self, grid, r1, r2, c1, c2, diff, counter, rows, cols):
        # Case 1: big grid → safe
        if rows > 1 and cols > 1:
            return diff in counter

        # Case 2: single row → only ends
        if rows == 1:
            return grid[r1][c1] == diff or grid[r1][c2] == diff

        # Case 3: single column → only ends
        if cols == 1:
            return grid[r1][c1] == diff or grid[r2][c1] == diff

        return False


