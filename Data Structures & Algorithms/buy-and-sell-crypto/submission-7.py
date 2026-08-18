class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                res = max(res, prices[i] - prices[buy])
        return res