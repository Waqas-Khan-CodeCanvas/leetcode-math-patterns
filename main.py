# 1878. Get Biggest Three Rhombus Sums in a Grid Medium

"""You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:

Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.


Example 1: 
Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]] 

Output: [228,216,211] 

Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above. - Blue: 20 + 3 + 200 + 5 = 228 - Red: 200 + 2 + 10 + 4 = 216 - Green: 5 + 200 + 4 + 2 = 211
from typing import List


Example 2: Input: grid = [[1,2,3],[4,5,6],[7,8,9]]

Output: [20,9,8] 

Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above. - Blue: 4 + 2 + 6 + 8 = 20 - Red: 9 (area 0 rhombus in the bottom right corner) - Green: 8 (area 0 rhombus in the bottom middle)


Example 3: Input: grid = [[7,7,7]] 

Output: [7] 

Explanation: All three possible rhombus sums are the same, so return [7]."""


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        
        for i in range(m):
            for j in range(n):
                # size 0 rhombus: single cell
                sums.add(grid[i][j])
                
                # try all possible sizes k of rhombus
                for k in range(1, min(m, n)):
                    if i - k < 0 or i + k >= m or j - k < 0 or j + k >= n:
                        break
                    
                    rhombus_sum = 0
                    
                    # sum top-right diagonal (i-k,j) to (i,j+k)
                    for t in range(k):
                        rhombus_sum += grid[i - k + t][j + t]
                    
                    # sum bottom-right diagonal (i,j+k) to (i+k,j)
                    for t in range(k):
                        rhombus_sum += grid[i + t][j + k - t]
                    
                    # sum bottom-left diagonal (i+k,j) to (i,j-k)
                    for t in range(k):
                        rhombus_sum += grid[i + k - t][j - t]
                    
                    # sum top-left diagonal (i,j-k) to (i-k,j)
                    for t in range(k):
                        rhombus_sum += grid[i - t][j - k + t]
                    
                    sums.add(rhombus_sum)
        
        # return the top 3 distinct sums descending
        return sorted(sums, reverse=True)[:3]
    
grid1 = [[3,4,5,1,3],
         [3,3,4,2,3],
         [20,30,200,40,10],
         [1,5,5,4,1],
         [4,3,2,2,5]]

sol = Solution()
print(sol.getBiggestThree(grid1))  # Output: [228, 216, 211]    