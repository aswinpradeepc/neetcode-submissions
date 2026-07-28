class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sor = sorted(set(nums))
        max_ = 0

        if len(sor) <= 1:
            return len(sor)
        res = []
        for i in sor:
            if not res:
                res.append(i)
                continue
            if i == res[-1] + 1:
                res.append(i)
            else:
                res = [i]
            max_ = max(len(res), max_)
        return max_        