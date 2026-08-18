class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 2 and s[0] == s[1]:
            return s
        elif len(s) <= 2:
            return s[0]
        res = 0
        resStr = ''

        def isPalindrome(string: str) -> bool:
            left = 0
            right = len(string) - 1

            while left < right:                
                if left < len(string) and right >= 0 and string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if isPalindrome(s[i:j + 1]) and j - i + 1 > res:
                    res = max(res, j - i + 1)
                    resStr = s[i:j + 1]
        return resStr