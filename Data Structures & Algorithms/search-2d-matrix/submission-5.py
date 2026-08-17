class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m*n-1

        while lo <= hi:
            mid = lo + (hi-lo)//2
            val = matrix[mid//n][mid%n]

            if val == target:
                return True
            elif target < val:
                hi = mid - 1
            else:
                lo = mid + 1
        return False


        
            



