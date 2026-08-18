class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stones[i] for i in range(len(stones))]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            if second < first:
                heapq.heappush(stones, - (first - second))
            
        if len(stones) == 0:
            return 0
        return abs(stones[0])