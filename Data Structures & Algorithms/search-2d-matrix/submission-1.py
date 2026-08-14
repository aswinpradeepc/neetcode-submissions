class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix[0]:
            return False

        # R:C::m:n -> m = rows (how many vertical)
        def mat_search(matrix):

            m = len(matrix)
            n = len(matrix[0])
            
            lo = 0
            hi = m - 1
            mid = hi//2

            while lo <= hi:
                if target <= matrix[mid][-1]:
                    if target >= matrix[mid][0]:
                        return mid
                    hi = mid - 1
                else: 
                    lo = mid + 1
                
                mid = lo + (hi - lo)//2
            return False
        k =  mat_search(matrix)

        l = 0
        r = len(matrix[k])-1
        mid = r//2
        while l <= r:
            if target == matrix[k][mid]:
                return True
            elif target >= matrix[k][mid]:
                l = mid + 1
            else: 
                r = mid - 1
            
            mid = l + (r-l)//2
        return False
            
            



