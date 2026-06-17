class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        unique = 0
        for word in strs:
            cnt = [0] * 26
            for c in word:
                cnt[ord(c) - ord('a')] += 1
            cnt_immutable = tuple(cnt)
            if cnt_immutable in res:
                res[cnt_immutable].append(word)
            else:
                res[cnt_immutable] = [word]
        return list(res.values())


                

        