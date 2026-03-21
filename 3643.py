"""
3643. Flip Square Submatrix Vertically

You are given an m x n integer matrix grid, and three integers x, y, and k.
The integers x and y represent the row and column indices of the top-left corner of a square submatrix and the integer k represents the size (side length) of the square submatrix.
Your task is to flip the submatrix by reversing the order of its rows vertically.
Return the updated matrix.


Example 1:
Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3
Output: [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]
Explanation:
The diagram above shows the grid before and after the transformation.

Example 2:
Input: grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2
Output: [[3,4,4,2],[2,3,2,3]]
Explanation:
The diagram above shows the grid before and after the transformation."""



from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            top, bottom = x + i, x + k - 1 - i
            for j in range(y, y + k):
                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]
        return grid


if __name__ == "__main__":
    s = Solution()

    # Example 1
    grid1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(s.reverseSubmatrix(grid1, 1, 0, 3))
    # Expected: [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]

    # Example 2
    grid2 = [[3,4,2,3],[2,3,4,2]]
    print(s.reverseSubmatrix(grid2, 0, 2, 2))
    # Expected: [[3,4,4,2],[2,3,2,3]]