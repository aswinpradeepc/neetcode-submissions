class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_ar = 0
        n = len(heights)

        ll = [-1] * len(heights)
        lr = [n] * len(heights)

        lst = []
        rst = []

        for i in range(n):
            while lst and heights[lst[-1]]>=heights[i]:
                lst.pop()
            if lst:
                ll[i] = lst[-1]
            lst.append(i)
        
        for i in range(n-1, -1, -1):
            while rst and heights[rst[-1]]>=heights[i]:
                rst.pop()
            if rst:
                lr[i] = rst[-1]
            rst.append(i)
        
        for i in range(n):
            ar = (lr[i] - ll[i] -1) * heights[i]
            max_ar = max(ar, max_ar)

        return max_ar
        


