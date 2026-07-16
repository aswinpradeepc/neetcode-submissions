class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1s = {}
        s2s = {}
        if len(s1) > len(s2):
            return False
        
        def dict_maker(s:str):
            res = {}
            for i in s:
                res[i] = res.get(i, 0) + 1
            return res

        l=0
        r = len(s1)
        s1s = dict_maker(s1)
        s2s = dict_maker(s2[l:r])
        while r <=len(s2):
            if s1s == s2s:
                return True
            s2s[s2[l]] = s2s[s2[l]] - 1
            if s2s[s2[l]] == 0:
                s2s.pop(s2[l])
            l += 1
            r += 1
            if r <= len(s2):
                s2s[s2[r - 1]] = s2s.get(s2[r-1], 0) + 1
        return False