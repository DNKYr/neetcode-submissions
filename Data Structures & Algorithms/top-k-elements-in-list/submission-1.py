class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for element in nums:
            if element in dic:
                dic[element] += 1
            else:
                dic[element] = 1

        buckets = [[] for _ in range(len(nums)+1)]
        ret = []
        for num, count in dic.items():
            buckets[count].append(num)
        for i in buckets[::-1]:
            for j in i:
                ret.append(j)
                if len(ret) == k:
                    return ret