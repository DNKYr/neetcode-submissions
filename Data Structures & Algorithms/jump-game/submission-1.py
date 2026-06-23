class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = [False for _ in range(n)]
        def dfs(i):
            if i == n-1:
                return True
            if visited[i] or nums[i] <= 0:
                return False
            
            visited[i] = True
            for jump in range(min(i + nums[i], n-1), 0, -1):
                possible = dfs(jump)
                if possible:
                    return True
            return False
        return dfs(0)
            
            

        