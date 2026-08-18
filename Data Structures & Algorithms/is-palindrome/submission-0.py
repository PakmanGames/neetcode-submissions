class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        j = len(s) - 1
        i = 0
        while i < j:
            if not s[i].isalnum() or not s[j].isalnum():
                if not s[i].isalnum():
                    i += 1
                if not s[j].isalnum():
                    j -= 1
            else:
                if s[j].lower() != s[i].lower():
                    return False
                i += 1
                j -= 1
        return True