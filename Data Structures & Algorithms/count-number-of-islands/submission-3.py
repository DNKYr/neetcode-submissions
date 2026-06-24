class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n, m, res = len(grid), len(grid[0]), 0
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for di, dj in direction:
                dfs(i + di, j + dj)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res


        
        