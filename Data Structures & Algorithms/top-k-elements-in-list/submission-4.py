class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)] 
        seen = {}
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        for i in seen:
            bucket[seen[i]].append(i)

        res = []
        for i in bucket[::-1]:
            res = res + i
            if len(res) >= k:
                return res[:k]
