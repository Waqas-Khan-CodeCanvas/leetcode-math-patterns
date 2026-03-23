"""1594. Maximum Non Negative Product in a Matrix
    You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.
    Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.
    Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.
    Notice that the modulo is performed after getting the maximum product.


Example 1:
Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.


Example 2:
Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).


Example 3:
Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0)."""



class Solution:
    def maxProductPath(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        max_dp = [[0]*n for _ in range(m)]
        min_dp = [[0]*n for _ in range(m)]
        
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        # First column
        for i in range(1, m):
            val = grid[i][0]
            max_dp[i][0] = max_dp[i-1][0] * val
            min_dp[i][0] = min_dp[i-1][0] * val
        
        # First row
        for j in range(1, n):
            val = grid[0][j]
            max_dp[0][j] = max_dp[0][j-1] * val
            min_dp[0][j] = min_dp[0][j-1] * val
        
        # Fill DP
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                
                candidates = [
                    max_dp[i-1][j] * val,
                    min_dp[i-1][j] * val,
                    max_dp[i][j-1] * val,
                    min_dp[i][j-1] * val
                ]
                
                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)
        
        result = max_dp[m-1][n-1]
        return result % MOD if result >= 0 else -1


# Test
if __name__ == "__main__":
    sol = Solution()
    
    grid = [[1,-2,1],
            [1,-2,1],
            [3,-4,1]]
    
    print(sol.maxProductPath(grid))  # Expected: 8