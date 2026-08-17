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
        
        def binary_search(space):
            r = len(space)-1
            l = 0
            while l<=r:
                m = l + (r-l)//2
                if space[m] == target:
                    return m
                elif target > space[m]:
                    l = m + 1
                else:
                    r = m -1
            return -1

        print(lo)
        if target >= nums[lo] and target <= nums[-1]:
            k = binary_search(nums[lo:])
            return -1 if k==-1 else k + lo
        else:
            k = binary_search(nums[:lo])
            return k