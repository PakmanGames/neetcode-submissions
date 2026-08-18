class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        left_s = ''
        right_s = ''
        while left < right:
            if s[left] != s[right]:
                left_s = s[:left] + s[left + 1:]
                right_s = s[:right] + s[right + 1:]
                break
            left += 1
            right -= 1
        left = 0
        right = len(left_s) - 1
        isLeft = True
        while left < right:
            if left_s[left] != left_s[right]:
                isLeft = False
                break
            left += 1
            right -= 1
        left = 0
        right = len(right_s) - 1
        isRight = True
        while left < right:
            if right_s[left] != right_s[right]:
                isRight = False
                break
            left += 1
            right -= 1
        if isLeft or isRight:
            return True
        return False