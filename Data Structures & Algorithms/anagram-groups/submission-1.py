class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            joined = ''.join(sorted(string))
            if joined in anagrams:
                anagrams[joined].append(string)
            else:
                anagrams[joined] = [string]
        
        res = []
        for ke, va in anagrams.items():
            res.append(va)
        return res