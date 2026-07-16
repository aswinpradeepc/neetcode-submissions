class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1s = {}
        s2s = {}
        
        def dict_maker(s:str):
            res = {}
            for i in s:
                res[i] = res.get(i, 0) + 1
            return res

        s1s = dict_maker(s1)
        l=0
        r = len(s1)
        while r <=len(s2):
            window = s2[l:r]
            s2s = dict_maker(window)
            if s1s == s2s:
                return True
            l +=1
            r+=1
        return False



