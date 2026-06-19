import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def find_distance(x, y):
            return math.sqrt(x * x + y * y)
        h = []
        for p in points:
            x = p[0]
            y = p[1]
            heapq.heappush_max(h, (find_distance(x, y), x, y))
            if len(h) > k:
                heapq.heappop_max(h)
        res = []
        while h:
            p = heapq.heappop_max(h)
            x = p[1]
            y = p[2]
            res.append([x, y])
        return res