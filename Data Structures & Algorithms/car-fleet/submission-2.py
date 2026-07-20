class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = []
        for i, val in enumerate(position):
            k = [val, speed[i]] # position, speed
            temp.append(k)
        temp.sort()
        time_left = []
        for i in temp:
            t = (target - i[0])/i[1]
            time_left.append(t)
        
        st = []
        time_left.reverse()
        print(time_left)
        for i in time_left:
            if st and i <= st[-1]:
                continue
            st.append(i)
        return len(st)


             