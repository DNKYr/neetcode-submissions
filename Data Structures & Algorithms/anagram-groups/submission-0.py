class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pair = {}
        res = []
        unique = 0
        for word in strs:
            cnt = [0] * 26
            for c in word:
                cnt[ord(c) - ord('a')] += 1
            cnt_immutable = tuple(cnt)
            if cnt_immutable in pair:
                res[pair[cnt_immutable]].append(word)
            else:
                res.append([word])
                pair[cnt_immutable] = unique
                unique += 1
        return res


                

        