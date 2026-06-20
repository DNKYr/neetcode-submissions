class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def recursion(target, i):
            if (i < 0):
                return target == 0
            return recursion(target - nums[i], i-1) + recursion(target + nums[i], i - 1)
        return recursion(target, n-1)
        