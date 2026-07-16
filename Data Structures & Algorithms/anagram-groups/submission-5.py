class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vals = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))

            if key in vals:
                vals[key].append(i)
            else:
                vals[key].append(i)
        return list(vals.values())