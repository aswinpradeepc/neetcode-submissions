class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            ss = "".join(sorted(i))
            if ss in seen:
                seen.get(ss).append(i)
            else:
                seen[ss] = [i]
        return list(seen.values())