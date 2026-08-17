class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo = 0
        hi = n - 1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if nums[mid] > nums[-1]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        def binary_search(l,r):
            while l<=r:
                m = l + (r-l)//2
                if nums[m] == target:
                    return m
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m -1
            return -1

        if target >= nums[lo] and target <= nums[-1]:
            return binary_search(l=lo, r=n-1)
        else:
            return binary_search(l=0,r=lo)