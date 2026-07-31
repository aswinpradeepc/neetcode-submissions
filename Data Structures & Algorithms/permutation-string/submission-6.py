class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def dict_maker(s: str):
            ss ={}
            for i in s:
                ss[i] = ss.get(i,0)+1
            return ss
        
        n1 = len(s1)
        n2 = len(s2)
        s1s = dict_maker(s1)
        s2s = dict_maker(s2[0:n1])
        if s1s == s2s:
            return True
        for i in range(n1, n2):
            s2s[s2[i-n1]] -= 1
            if s2s[s2[i-n1]] ==0:
                s2s.pop(s2[i-n1])
            s2s[s2[i]] = s2s.get(s2[i], 0) +1
            if s1s == s2s:
                return True
        
        return False

