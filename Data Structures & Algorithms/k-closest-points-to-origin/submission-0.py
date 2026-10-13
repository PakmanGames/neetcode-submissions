class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points: # O(n)
            c = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (c, [x, y])) # O(logn)
        
        # print(heap)
        res = []
        for _ in range(k): # O(k)
            res.append(heapq.heappop(heap)[1])
        return res
        # Time: O(k + nlogn)
        # Space: O(n)