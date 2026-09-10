class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        res = []

        for _ in range(k):
            maxx = 0
            max_ke = None
            for ke, va in freq.items():
                if va > maxx:
                    maxx = va
                    max_ke = ke
            del freq[max_ke]
            res.append(max_ke)
        return res