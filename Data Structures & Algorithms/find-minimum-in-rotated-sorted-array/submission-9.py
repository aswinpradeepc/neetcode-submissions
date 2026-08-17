class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo = 0
        hi = n - 1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if nums[mid] > nums[-1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[lo]