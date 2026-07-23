class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        seen = {}
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        
        print(seen)

        for i in seen:
            if seen[i] not in res:
                res[seen[i]] = [i]
            else:
                res[seen[i]].append(i)
        
        print(res)
        
        l = sorted(list(res))
        l = l[::-1]
        print(l)
        fin = []
        for i in l:
            if len(fin) <= k:
                m = res[i]
                print("m", m)
                for j in m:
                    fin.append(j)
        
        return fin[:k]

                
