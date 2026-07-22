class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vals = {}
        res = []
        for i in strs:
            s = sorted(list(i))
            k = ''
            for j in s:
                k+=j           
            if k not in vals:
                vals[k] = [i]
            elif k in vals:
                vals[k].append(i)
        print(vals)
        for i in vals.values():
            res.append(i)
        return res
