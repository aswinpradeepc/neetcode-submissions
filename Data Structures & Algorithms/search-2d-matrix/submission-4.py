class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # R:C::m:n -> m = rows (how many vertical)
        def mat_search(matrix):

            m = len(matrix)
            n = len(matrix[0])
            
            lo = 0
            hi = m - 1

            while lo <= hi:
                mid = lo + (hi - lo)//2
                if target <= matrix[mid][-1]:
                    if target >= matrix[mid][0]:
                        return matrix[mid]
                    hi = mid - 1
                else: 
                    lo = mid + 1
                
            return False
        k =  mat_search(matrix)
        if not k:
            return False

        l = 0
        r = len(k)-1
        mid = r//2
        while l <= r:
            if target == k[mid]:
                return True
            elif target >= k[mid]:
                l = mid + 1
            else: 
                r = mid - 1
            
            mid = l + (r-l)//2
        return False
            
            



