class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)

        left = 1
        right = maximum
        res = maximum
        while left <= right:
            currTime = 0
            mid = (left + right) // 2
            for pile in piles:
                currTime += math.ceil(pile / mid)
                if currTime > h:
                    break
            if currTime <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res