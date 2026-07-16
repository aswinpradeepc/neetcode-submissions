class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0,len(prices)-1):
            r = len(prices)-1
            while i<r:
                profit = prices[r]-prices[i]
                print(prices[r],prices[i])
                max_profit = max(profit, max_profit)
                r = r-1
        return max_profit
