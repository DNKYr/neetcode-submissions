class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hold = 0
        for num in nums:
            hold = num ^ hold
        return hold
        