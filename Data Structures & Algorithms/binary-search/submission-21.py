class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        hi = n -1   
        lo = 0

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid -1
            
        return -1



            