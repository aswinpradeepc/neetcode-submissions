class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        rmax = [0] *n
        rmax[-1] = prices[-1]
        for i in range(n-2, -1, -1):
            rmax[i] = max(prices[i], rmax[i+1])

        m = 0
        for i in range(n):
            m = max(m, rmax[i]-prices[i])
        return m

