class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        hi = n -1   
        lo = 0

        mid = n//2
        while True:
            if nums[lo] > target or nums[hi] < target:
                return -1
            elif nums[mid] == target:
                return mid
            # elif mid == lo:
            #     return -1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid -1
            
            mid = lo + (hi - lo) // 2



            