class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL, res = len(grid), len(grid[0]), 0
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROW or j >= COL or not grid[i][j]:
                return 0
            area = 1
            grid[i][j] = 0
            for di, dj in direction:
                area += dfs(i + di, j + dj)
            return area
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        return res

            
        