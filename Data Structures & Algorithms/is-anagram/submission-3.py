class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def dict_maker(l: str):
            ss = {}
            for i in l:
                if i in ss:
                    ss[i] += 1
                else:
                    ss[i] = 1
            return ss
        sss = dict_maker(s)
        ttt = dict_maker(t)
        if sss == ttt:
            return True
        return False