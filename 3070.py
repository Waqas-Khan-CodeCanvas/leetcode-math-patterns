# 3070. Count Submatrices with Top-Left Element and Sum Less Than k

"""
    You are given a 0-indexed integer matrix grid and an integer k.
    Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.


    Example 1:
    Input: grid = [[7,6,3],[6,6,1]], k = 18
    Output: 4
    Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.
    
    
    Example 2:
    Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
    Output: 6
    Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.
 """




class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # Build prefix sum
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                ps[i+1][j+1] = (
                    grid[i][j]
                    + ps[i][j+1]
                    + ps[i+1][j]
                    - ps[i][j]
                )
        
        # Count valid submatrices
        count = 0
        for i in range(m):
            for j in range(n):
                if ps[i+1][j+1] <= k:
                    count += 1
        
        return count


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    grid1 = [[7,6,3],[6,6,1]]
    k1 = 18
    print("Output 1:", sol.countSubmatrices([row[:] for row in grid1], k1))  # copy grid
    
    # Test Case 2
    grid2 = [[7,2,9],[1,5,0],[2,6,6]]
    k2 = 20
    print("Output 2:", sol.countSubmatrices([row[:] for row in grid2], k2))