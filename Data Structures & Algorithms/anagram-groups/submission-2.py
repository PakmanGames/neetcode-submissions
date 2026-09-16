class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sortedw = ''.join(sorted(word))
            if sortedw in anagrams:
                anagrams[sortedw].append(word)
            else:
                anagrams[sortedw] = [word]
        
        return [val for _, val in anagrams.items()]
        # O(n) time we must check every element in strs
        # O(n) space what if no matching pairs of anagrams