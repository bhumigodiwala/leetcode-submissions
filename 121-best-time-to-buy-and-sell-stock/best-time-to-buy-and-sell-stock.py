class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            elif prices[sell] > prices[buy]:
                curr_profit = prices[sell] - prices[buy]
                if curr_profit > max_profit:
                    max_profit = curr_profit
            sell += 1
        return max_profit