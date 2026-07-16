class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, val in enumerate(nums):
            if val > 0:
                break
            
            if i > 0 and val == nums[i -1]:
                continue

            l = i + 1
            r = len(nums)-1
            while l < r:
                t = nums[l] + nums[r] + nums[i]
                if t > 0:
                    r -= 1
                elif t < 0:
                    l += 1
                elif t ==0:
                    res.append([val,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    
        return res





        