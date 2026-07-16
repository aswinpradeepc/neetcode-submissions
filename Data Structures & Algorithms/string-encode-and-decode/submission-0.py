class Solution:

    def encode(self, strs: List[str]) -> str:
        hehe = ""
        for i in strs:
            for k in i:
                hehe += str(ord(k))
                hehe += "#"
            hehe += "%"
        return hehe

    def decode(self, s: str) -> List[str]:
        haha = ""
        word = ""
        res = []
        for i in s:
            if i == "%":
                # haha += " "
                res.append(haha)
                haha = ""
            if i not in ["#", "%"]:
                word += str(i)
            if i == "#":
                haha += chr(int(word))
                word = ""
        return res


