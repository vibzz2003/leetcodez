class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(n))for j in range(n)]

        total_inc = 0

        for i in range(n):
            for j in range(n):
                max_height = min(row_max[i], col_max[j])
                total_inc += max_height - grid[i][j]
        
        return total_inc