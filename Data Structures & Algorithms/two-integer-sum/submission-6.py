class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            numss = nums.copy()
            print(numss)
            numss.pop(i)
            numss.insert(i,0.5)
            print(numss)
            if (target - nums[i]) in numss:
                return [i, numss.index(target - nums[i])]