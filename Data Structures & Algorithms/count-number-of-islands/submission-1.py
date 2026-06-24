from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
        n, m, res = len(grid), len(grid[0]), 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        def is_valid_next(i, j):
            return i >= 0 and j >= 0 and i < n and j < m and grid[i][j] == "1" and not visited[i][j]
        q = deque()
        for i in range(n):
            for j in range(m):
                if is_valid_next(i, j):
                    q.append((i, j))
                    while len(q) > 0:
                        cur_i, cur_j = q.popleft()
                        visited[cur_i][cur_j] = True
                        for r, c in direction:
                            next_i = cur_i + r
                            next_j = cur_j + c
                            if is_valid_next(next_i, next_j):
                                q.append((next_i, next_j))
                    res += 1
        return res


                
        
        