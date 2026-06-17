class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res, l, r = 0, 0, 0
        present_letter = set()
        while r < n:
            cur_letter = s[r]
            last_letter = s[l]
            if cur_letter not in present_letter:
                present_letter.add(cur_letter)
                r += 1
            else:
                res = max(res, r - l)
                l += 1
                present_letter.remove(last_letter)


        return max(res, r - l)