class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        res = 0
        l,r=0,0

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r],0) + 1

            while ((r-l+1) - max(seen.values())) > k:
                seen[s[l]] = seen[s[l]] - 1
                l+=1
            res = max(r-l+1, res)
        return res
            

            
        
        

