class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        zero_loc = set()
        for (i, num) in enumerate(nums[1:]):
            if num != 0:
                product *= num
            else:
                zero_loc.add(i + 1)
        if len(zero_loc) >= 2:
            res = [0 for _ in nums]
        elif len(zero_loc) == 1:
            res = []
            for (i, num) in enumerate(nums):
                if i not in zero_loc:
                    res.append(0)
                else:
                    res.append(product)
        else:
            res = []
            for (i, num) in enumerate(nums):
                res.append(int (product / num))
        return res
     