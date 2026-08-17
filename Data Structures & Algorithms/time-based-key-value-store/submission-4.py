class TimeMap:

    def __init__(self):
        self.stor = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stor.setdefault(key, []).append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stor:
            return ""

        space = self.stor[key]
        n = len(self.stor[key])
        l,r = 0, n-1
        ans = ""
        while l<=r:
            mid = l+(r-l)//2
            if space[mid][0] <= timestamp:
                ans = space[mid][1]
                l = mid + 1
            else:
                r = mid -1
        return ans


        
