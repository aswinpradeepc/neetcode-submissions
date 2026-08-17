class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev = nums[0]
        for i,val in enumerate(nums):
            if val < prev:
                return val
        return prev
        