"""2352. Equal Row and Column Pairs
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]


Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""



from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Convert rows to tuples and count their frequencies
        row_count = {}
        for r in range(n):
            row_tuple = tuple(grid[r])
            row_count[row_tuple] = row_count.get(row_tuple, 0) + 1
        
        result = 0
        
        # For each column, create a tuple and check in row_count
        for c in range(n):
            col_tuple = tuple(grid[r][c] for r in range(n))
            if col_tuple in row_count:
                result += row_count[col_tuple]
        
        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    grid = [
        [3, 2, 1],
        [1, 7, 6],
        [2, 7, 7]
    ]
    print("Number of equal row and column pairs:", solution.equalPairs(grid))