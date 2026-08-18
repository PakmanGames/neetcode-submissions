class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        left = 0
        res = 0
        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[left])
                left += 1
            ss.add(s[r])
            res = max(res, r - left + 1)
        return res