class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        index = []
        for i, val in enumerate(nums):
            if val != 0:
                prod *= val
            if val == 0:
                index.append(i)
        res = []
        for i, val in enumerate(nums):
            if len(index)<=0:
                res.append(int(prod/val))
            if len(index) == 1 and val ==  0:
                res.append(prod)
            if len(index) == 1 and val !=0:
                res.append(0)
            if len(index) > 1:
                res.append(0)
        return res 