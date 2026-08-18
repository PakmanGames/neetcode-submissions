class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        res = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                res = max(res, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return res