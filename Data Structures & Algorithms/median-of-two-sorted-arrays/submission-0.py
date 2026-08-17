class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = nums1+nums2
        s.sort()
        n =len(s)
        if n%2==0:
            k =(n-1)//2
            return (s[k] + s[k+1])/2
        else:
            return s[(n-1)//2]
        
