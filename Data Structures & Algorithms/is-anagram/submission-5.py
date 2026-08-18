class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = {}
        for letter in s:
            freq_s[letter] = freq_s.get(letter, 0) + 1
        
        freq_t = {}
        for letter in t:
            if letter not in freq_s:
                return False
            freq_t[letter] = freq_t.get(letter, 0) + 1
        
        for ke, val in freq_s.items():
            if freq_t.get(ke) != val:
                return False
        return True