class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        k=False
        for i in nums:
            count = count +1
            for j in nums[count:]:
                if j == i:
                    k = True
        return k
                
            
        
    
                    
