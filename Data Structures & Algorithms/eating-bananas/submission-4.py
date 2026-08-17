class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        res = hi = max(piles)
        while lo<=hi:
            mid = lo + (hi-lo)//2
            
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            if time <=h:
                hi=mid-1
                res = min(res,mid)
            else:
                lo=mid+1
        return res
            



        