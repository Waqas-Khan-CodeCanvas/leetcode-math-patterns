""" 3546. Equal Sum Grid Partition I

    You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:Each of the two resulting sections formed by the cut is non-empty.
    The sum of the elements in both sections is equal.
    Return true if such a partition exists; otherwise return false.


Example 1:
Input: grid = [[1,4],[2,3]]
Output: true

Explanation:A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.


Example 2:
Input: grid = [[1,3],[2,4]]
Output: false

Explanation:No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

"""



from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # Check horizontal cuts
        curr = 0
        for i in range(m - 1):
            curr += sum(grid[i])
            if curr == target:
                return True
        
        # Check vertical cuts
        curr = 0
        col_sums = [0] * n
        
        for j in range(n):
            for i in range(m):
                col_sums[j] += grid[i][j]
        
        for j in range(n - 1):
            curr += col_sums[j]
            if curr == target:
                return True
        
        return False


#  Test
if __name__ == "__main__":
    sol = Solution()
    
    grid1 = [[1, 4], [2, 3]]
    grid2 = [[1, 3], [2, 4]]
    
    print(sol.canPartitionGrid(grid1))  # Expected: True
    print(sol.canPartitionGrid(grid2))  # Expected: False