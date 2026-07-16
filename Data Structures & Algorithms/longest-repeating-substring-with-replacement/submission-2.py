class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        res = 0
        l,r=0,0
        def max_seen(d:dict):
            max_ = 0
            for i in d:
                max_ = max(d[i], max_)
            return max_

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r],0) + 1

            max_ = max_seen(seen)
            while ((r-l+1) - max_) > k:
                seen[s[l]] = seen[s[l]] - 1
                l+=1
            res = max(r-l+1, res)
        return res
            

            
        
        

