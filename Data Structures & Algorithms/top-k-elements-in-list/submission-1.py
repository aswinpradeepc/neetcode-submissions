class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen [i] = 1
        res = []
        for val in seen.values():
            res.append(val)
        res.sort(reverse=True)
        print(res)
        res = res[:k]
        print(res)
        ress = []
        for val in seen:
            if seen[val] in res:
                ress.append(val)
        return ress
        