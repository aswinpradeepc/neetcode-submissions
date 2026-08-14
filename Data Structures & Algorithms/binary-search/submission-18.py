class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        hi = n -1   
        lo = 0

        mid = n//2
        while lo <= hi:
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid -1
            
            mid = lo + (hi - lo) // 2
        return -1



            