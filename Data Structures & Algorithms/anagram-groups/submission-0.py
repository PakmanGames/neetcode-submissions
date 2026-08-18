class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            word = "".join(sorted(s))
            if word not in res:
                res[word] = []
            res[word].append(s)
        
        return list(res.values())