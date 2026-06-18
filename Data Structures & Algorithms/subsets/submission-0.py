class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def recursion(current_set):
            if not current_set:
                return
            if current_set not in res:
                res.append(current_set)
                for i in range(len(current_set)):
                    recursion(current_set[:i] + current_set[i+1:])
        recursion(nums)
        return res
        