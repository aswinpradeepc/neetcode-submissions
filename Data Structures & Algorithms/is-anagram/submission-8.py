class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = "".join(sorted(list(s)))
        tt = "".join(sorted(list(t)))

        return ss == tt
