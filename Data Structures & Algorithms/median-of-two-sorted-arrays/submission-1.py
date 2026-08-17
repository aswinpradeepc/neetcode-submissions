class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2

        if len(nums1) > len(nums2):
            a, b = b, a
        
        na = len(a)
        nb = len(b)
        half = (na+nb)//2

        l, r = 0, na-1
        while True:
            i = (l+r) // 2 # mid of short array
            j = half - i - 2 # index of partition on long array

            Aleft = a[i] if i >= 0 else float("-infinity")
            Aright = a[i+1] if (i+1) < na else float("infinity")
            Bleft = b[j] if j >= 0 else float("-infinity")
            Bright = b[j+1] if (j+1) < nb else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if (na+nb)%2:
                    return (min(Aright, Bright))
                return ((max(Aleft,Bleft)+min(Aright,Bright))/2)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

            
        





