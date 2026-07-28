class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        l = len(set(nums))

        if n > l:
            return True
        return False
