class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        res = []
        p_product = 1
        s_product = 1
        for i in range(len(nums)):
            last_i = len(nums) - i - 1
            prefix.append(p_product)
            suffix.insert(0, s_product)
            p_product *= nums[i]
            s_product *= nums[last_i]
        
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res
        
            
            


        