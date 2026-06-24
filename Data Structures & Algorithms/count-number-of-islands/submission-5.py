from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
        n, m, res = len(grid), len(grid[0]), 0
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            while q:
                cur_i, cur_j = q.popleft()
                for di, dj in direction:
                    n_i = di + cur_i
                    n_j = dj + cur_j
                    if n_i < 0 or n_j < 0 or n_i >= n or n_j >= m or grid[n_i][n_j] == "0":
                        continue
                    q.append((n_i, n_j))
                    grid[n_i][n_j] = "0"
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        return res


                
        
        