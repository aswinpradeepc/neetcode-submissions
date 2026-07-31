class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0,1
        n = len(s)
        if n <= 1:
            return n
        m = 0
        while r < n:
            if s[r] not in s[l:r]:
                r+=1
            else:
                l+=1
            m = max(m, r-l)
        return m 
                

