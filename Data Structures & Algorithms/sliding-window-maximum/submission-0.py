class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        res.append(max(nums[:k]))
        for r in range(k+1,len(nums)+1):
            l+=1
            res.append(max(nums[l:r]))
        return res
        