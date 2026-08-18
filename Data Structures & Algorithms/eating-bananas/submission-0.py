class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 10 ** 9
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            curr = 0
            for i in range(len(piles)):
                if curr > h:
                    break
                curr += math.ceil(piles[i] / mid)
            if curr <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res