class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        hi = n -1   
        lo = 0
        
        mid = n//2
        while target != nums[mid]:
            if nums[lo] > target or nums[hi] < target:
                return -1
            elif nums[mid] == target:
                return mid
            elif nums[hi] == target:
                return hi
            elif mid == lo:
                return -1
            elif target > nums[mid]:
                lo = mid
            else:
                hi = mid
            
            mid = lo + (hi - lo) // 2
            
        
        return mid


            