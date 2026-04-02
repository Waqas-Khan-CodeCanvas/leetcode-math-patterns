"""3418. Maximum Amount of Money Robot Can Earn
You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.
The grid contains a value coins[i][j] in each cell:
If coins[i][j] >= 0, the robot gains that many coins.
If coins[i][j] < 0, the robot encounters a robber, and the robber steals the absolute value of coins[i][j] coins.
The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.
Note: The robot's total coins can be negative.
Return the maximum profit the robot can gain on the route.


Example 1:
Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
Output: 8
Explanation:
An optimal path for maximum coins is:
Start at (0, 0) with 0 coins (total coins = 0).
Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1).
Move to (1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total coins = 1).
Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4).
Move to (2, 2), gaining 4 coins (total coins = 4 + 4 = 8).


Example 2:
Input: coins = [[10,10,10],[10,10,10]]
Output: 40
Explanation:
An optimal path for maximum coins is:
Start at (0, 0) with 10 coins (total coins = 10).
Move to (0, 1), gaining 10 coins (total coins = 10 + 10 = 20).
Move to (0, 2), gaining another 10 coins (total coins = 20 + 10 = 30).
Move to (1, 2), gaining the final 10 coins (total coins = 30 + 10 = 40).

"""


from typing import List
from math import inf

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        dp = [[[-inf] * 3 for _ in range(n)] for _ in range(m)]
        
        # Initialize start
        for k in range(3):
            if coins[0][0] >= 0:
                dp[0][0][k] = coins[0][0]
            else:
                dp[0][0][k] = 0 if k > 0 else coins[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                for k in range(3):
                    val = coins[i][j]
                    
                    best_prev = -inf
                    if i > 0:
                        best_prev = max(best_prev, dp[i-1][j][k])
                    if j > 0:
                        best_prev = max(best_prev, dp[i][j-1][k])
                    
                    if best_prev != -inf:
                        dp[i][j][k] = best_prev + val
                    
                    # Neutralize if negative
                    if val < 0 and k > 0:
                        best_prev_neutral = -inf
                        if i > 0:
                            best_prev_neutral = max(best_prev_neutral, dp[i-1][j][k-1])
                        if j > 0:
                            best_prev_neutral = max(best_prev_neutral, dp[i][j-1][k-1])
                        
                        if best_prev_neutral != -inf:
                            dp[i][j][k] = max(dp[i][j][k], best_prev_neutral)
        
        return int(max(dp[m-1][n-1]))

# test cases
if __name__ == "__main__":
    sol = Solution()
    
    coins1 = [[0,1,-1],[1,-2,3],[2,-3,4]]
    print("Output 1:", sol.maximumAmount(coins1))  # Expected: 8
    
    coins2 = [[10,10,10],[10,10,10]]
    print("Output 2:", sol.maximumAmount(coins2))  # Expected: 40