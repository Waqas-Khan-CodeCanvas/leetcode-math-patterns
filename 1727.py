# 1727. Largest Submatrix With Rearrangements

"""You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.


Example 1:
Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4

Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.


Example 2:
Input: matrix = [[1,0,1,0,1]]
Output: 3

Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.


Example 3:
Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
"""

from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0

        for i in range(m):

            # Update heights of histogram
            for j in range(n):
                if matrix[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1

            # Sort heights in descending order
            sorted_heights = sorted(heights, reverse=True)

            # Calculate max possible area
            for width in range(n):
                area = sorted_heights[width] * (width + 1)
                ans = max(ans, area)

        return ans


# Testing the solution

def run_tests():
    sol = Solution()

    test_cases = [
        ([[0,0,1],[1,1,1],[1,0,1]], 4),
        ([[1,0,1,0,1]], 3),
        ([[1,1,0],[1,0,1]], 2),
        ([[1,1,1],[1,1,1]], 6),
    ]

    for i, (matrix, expected) in enumerate(test_cases):
        result = sol.largestSubmatrix(matrix)
        print(f"Test Case {i+1}")
        print("Matrix:", matrix)
        print("Expected:", expected)
        print("Result:", result)
        print("PASS" if result == expected else "FAIL")
        print("-"*40)


if __name__ == "__main__":
    run_tests()