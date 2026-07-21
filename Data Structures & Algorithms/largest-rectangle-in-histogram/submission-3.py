class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] # index, height
        n = len(heights)
        leftMost = [-1] * n
        rightMost = [n] * n

        for i in range(len(heights)):
            while st and st[-1][1] >= heights[i]:
                st.pop()

            if st:
                leftMost[i] = st[-1][0]

            st.append([i,heights[i]])

        st =[]
        for i in range(n-1, -1, -1):
            while st and st[-1][1] >= heights[i]:
                st.pop()

            if st:
                rightMost[i] = st[-1][0]

            st.append([i,heights[i]])
        maxar = 0
        for i in range(len(heights)):
            maxar = max(maxar, (rightMost[i]-leftMost[i] - 1)*heights[i])

        return maxar
                