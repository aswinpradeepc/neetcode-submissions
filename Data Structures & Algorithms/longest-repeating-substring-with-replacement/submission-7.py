class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        seen = {}
        maxf = 0
        res = 0
        l=0
        for r, val in enumerate(s):
            seen[val] = seen.get(val, 0) + 1
            maxf = max(seen[val], maxf)

            while (r-l+1)-maxf > k:
                seen[s[l]] -= 1
                l+=1
            
            res = max(res, r-l+1)
        
        return res
            

            
            