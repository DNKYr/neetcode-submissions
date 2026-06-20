class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def memoization(recur):
            cache = {}
            def memo(target, i):
                if (target, i) not in cache:
                    cache[(target, i)] = recur(target, i)
                return cache[(target, i)]
            return memo
        def recur(target, i):
            if i < 0:
                return target == 0
            return recur(target - nums[i], i-1) + recur(target + nums[i], i - 1)
        optimized_recur = memoization(recur)
        return optimized_recur(target, n-1)
                