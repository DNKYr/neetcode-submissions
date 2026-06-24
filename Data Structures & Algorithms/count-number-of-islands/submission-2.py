class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n, m, res = len(grid), len(grid[0]), 0
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def is_valid_next(i, j):
            return i >= 0 and j >= 0 and i < n and j < m and grid[i][j] == "1" 
        def dfs(i, j):
            grid[i][j] = "0"
            for c, r in direction:
                next_i = i + c
                next_j = j + r
                if is_valid_next(next_i, next_j):
                    dfs(next_i, next_j)
        for i in range(n):
            for j in range(m):
                if is_valid_next(i, j):
                    dfs(i, j)
                    res += 1
        return res


        
        