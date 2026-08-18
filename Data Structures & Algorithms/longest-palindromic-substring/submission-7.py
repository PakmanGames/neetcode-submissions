class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStr = ''
        res = 0

        for i in range(len(s)):
            left = i
            right = i

            # odd letter case:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res:
                    res = right - left + 1
                    resStr = s[left:right + 1]
                left -= 1
                right += 1
            
            # even letter case:
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res:
                    res = right -left + 1
                    resStr = s[left: right + 1]
                left -= 1
                right += 1
        
        return resStr