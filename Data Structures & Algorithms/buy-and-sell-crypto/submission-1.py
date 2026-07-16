class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_price = prices[-1]
        for i in range(len(prices)-1,-1,-1):
            max_price=max(prices[i], max_price)
            max_profit = max(max_profit, max_price - prices[i])
        return max_profit

