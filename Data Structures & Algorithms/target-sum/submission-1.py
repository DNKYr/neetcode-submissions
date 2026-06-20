class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dfs(i, c_sum):
            if (i >= n):
                if c_sum == target:
                    return 1
                return 0
            return dfs(i+1, c_sum + nums[i]) + dfs(i+1, c_sum - nums[i])
        return dfs(0, 0)
        