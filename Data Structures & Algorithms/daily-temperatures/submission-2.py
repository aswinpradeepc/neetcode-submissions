class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = [] # index, val
        res = [0] * len(temperatures)

        for i, val in enumerate(temperatures):
            while st and st[-1][1] < val:
                sti, stval = st.pop()
                res[sti] = i - sti
            st.append([i,val])
        return res
        

