class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) # minheap but we need max heap so -1 in prev line
        while len(stones) > 1:
            s1 = -1 * heapq.heappop(stones)
            s2 = -1 * heapq.heappop(stones)
            if s1 < s2:
                heapq.heappush(stones, -1 * (s2 - s1))
            elif s2 < s1:
                heapq.heappush(stones, -1 * (s1 - s2))
        return -1 * stones[0] if len(stones) != 0 else  0
        # O(n) space heapify doesnt use nlogn space
        # O(nlogn) time