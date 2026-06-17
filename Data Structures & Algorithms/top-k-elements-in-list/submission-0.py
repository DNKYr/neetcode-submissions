class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for element in nums:
            if element in dic:
                dic[element] += 1
            else:
                dic[element] = 1

        sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        ret = []
        cnt = 0
        for value in sorted_dic.keys():
            if cnt >= k:
                return ret
            cnt += 1
            ret.append(value)
        return ret