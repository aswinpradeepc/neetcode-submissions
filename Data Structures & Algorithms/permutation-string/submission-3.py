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
        for i in range(0, n2):

            s2s = dict_maker(s2[i:i+n1])
            print(s2[i:i+n1])

            if s1s == s2s:
                return True
        
        return False

