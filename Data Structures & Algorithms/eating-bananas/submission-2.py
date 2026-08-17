class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = max(piles)

        # def kcheck(rate: int):
        #     time = 0
        #     i = 0
        #     while time<=h and i<n:
        #         time += math.ceil(piles[i]/rate)
        #         i+=1
        #     if time > h:
        #         return False
        #     else:
        #         return True
                
        lo = 1
        hi = m
        res=m
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
            



        