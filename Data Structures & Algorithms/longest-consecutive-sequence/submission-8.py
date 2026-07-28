class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sor = sorted(set(nums))
        max_ = 1

        streak = 1
        for i in range(1, len(sor)):
            if sor[i] == sor[i-1] + 1:
                streak+=1
            else:
                streak = 1
            max_ = max(streak, max_)
        return max_        