class Solution:
    def findMin(self, nums: List[int]) -> int:
        hi = len(nums)-1
        lo = 0
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid]<=nums[-1]:
                hi = mid -1
            else:
                lo = mid + 1
        return nums[lo]