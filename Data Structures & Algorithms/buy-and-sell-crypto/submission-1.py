class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = buy + 1
        res = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                res = max(res, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return res