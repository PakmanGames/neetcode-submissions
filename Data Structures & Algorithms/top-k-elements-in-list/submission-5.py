from heapq import heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num,freq in freq.items():
            if len(heap) < k:
                heappush(heap, (freq, num))
                continue

            if freq > heap[0][0]:
                heappop(heap)
                heappush(heap, (freq, num))
        
        return [i[1] for i in heap]
            

            















