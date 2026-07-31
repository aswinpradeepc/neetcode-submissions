class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0,1
        n = len(s)
        if n <= 1:
            return n
        m = 0
        seen = set()
        seen.add(s[l])
        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
            else:
                seen.remove(s[l])
                l+=1
            m = max(m, r-l)
        return m 
                

