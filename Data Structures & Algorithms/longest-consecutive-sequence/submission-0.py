class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = sorted(list(set(nums)))
        
        # Start the result list with the first element
        res = [nums[0]]  
        maxx = 1
        
        # Start checking from the second element
        i = 1
        while i < len(nums):
            # If it's consecutive, add it to your tracking list
            if nums[i] == nums[i-1] + 1:
                res.append(nums[i])
            else:
                # Streak broken: check max length
                maxx = max(maxx, len(res))
                
                # Reset the tracking list to START with the new number
                res = [nums[i]]  
            
            i += 1
            
        # Catch the final streak length after the loop ends
        maxx = max(maxx, len(res))
        
        return maxx