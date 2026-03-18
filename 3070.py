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