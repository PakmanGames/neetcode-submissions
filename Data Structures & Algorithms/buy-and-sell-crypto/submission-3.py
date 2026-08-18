class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        out: 6
        [10,1,5,6,7,1]
         0  1 2 3 4 5

        profit = 0
        buy_day = 0 # first index
        loop over each element start index 1:
            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day
            else:
                curr_profit = prices[sell_day] - prices[buy_day]
                profit = max(profit, curr_profit)

        return profit
        '''
        profit = 0
        buy_day = 0 # first index
        for sell_day in range(1, len(prices)):
            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day
            else:
                curr_profit = prices[sell_day] - prices[buy_day]
                profit = max(profit, curr_profit)

        return profit
        '''
        [10,1,5,6,7,1]
         0  1 2 3 4 5

        p = 0
        b = 0

        s = 1
        1 < 10 --> b = 1

        s = 2
        5 < 1 --> curp = 4
        4 > 0 --> p = 4

        s = 3
        6 < 1 --> curp = 5
        5 > 4 --> p = 5

        s = 4
        7 < 1 --> curp = 6
        6 > 5 --> p = 6

        s = 5
        1 < 1 --> curp = 0
        0 > 6 --> p = 6

        s = 6
        [1, 6)

        return 6
        '''