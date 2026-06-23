class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]

        dp[0] = True
        for index, num in enumerate(nums):
            for i in range(min(index + num, n - 1), 0, -1):
                dp[i] = dp[index]
        return dp[-1]

        