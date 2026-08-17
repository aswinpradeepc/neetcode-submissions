class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = max(piles)

        def kcheck(rate: int):
            time = 0
            i = 0
            while time<=h and i<n:
                time += math.ceil(piles[i]/rate)
                i+=1
            if i<=n and time>h:
                print(time, rate,"f")
                return False
            else:
                print(time,rate, "t")
                return True
                
        lo = 1
        hi = m
        res=m
        while lo<=hi:
            mid = lo + (hi-lo)//2
            # print(mid)
            if kcheck(mid):
                hi=mid-1
                res = min(res,mid)
            else:
                lo=mid+1
        return res
            



        