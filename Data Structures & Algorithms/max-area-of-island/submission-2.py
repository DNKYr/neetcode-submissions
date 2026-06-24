from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        ROW, COL = len(grid), len(grid[0])
        res = 0

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            grid[i][j] = 0
            area = 0
            while q:
                cur_r, cur_c = q.popleft()
                area += 1
                for dr, dc in directions:
                    next_r, next_c = cur_r + dr, cur_c + dc
                    if next_r < 0 or next_c < 0 or next_r >= ROW or next_c >= COL or not grid[next_r][next_c]:
                        continue
                    q.append((next_r, next_c))
                    grid[next_r][next_c] = 0
            return area
                
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]:
                    res = max(bfs(i, j),res)

        return res
        