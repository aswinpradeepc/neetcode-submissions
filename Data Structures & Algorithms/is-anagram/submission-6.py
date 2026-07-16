class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        for i in set(s).union(set(t)):
            if ls.count(i) != lt.count(i):
                return False
        return True
