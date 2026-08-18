class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unq_s = {}
        unq_t = {}
        for letter in s:
            if letter in unq_s:
                unq_s[letter] += 1
            else:
                unq_s[letter] = 1

        for letter in t:
            if letter in unq_t:
                unq_t[letter] += 1
            else:
                unq_t[letter] = 1

        for letter in s:
            if letter not in unq_t:
                return False
            if letter not in t:
                return False
            if letter in t:
                if unq_s[letter] != unq_t[letter]:
                    return False

        for letter in t:
            if letter not in s:
                return False

        return True