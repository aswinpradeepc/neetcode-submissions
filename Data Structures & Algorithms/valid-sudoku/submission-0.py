class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in board:
            seen = {}
            for j in i:
                seen[j] = 1 + seen.get(j, 0)
                if j != "." and seen[j] > 1:
                    return False

        for i in range(1,9):
            seen = {}
            for j in board:
                num = j[i]
                seen[j[i]] = 1 + seen.get(num, 0)
                if j[i] != "." and seen[j[i]] > 1:
                    print(seen[j[i]])
                    return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                gridseen = {}
                for k in range(0,3):
                    for l in range(0,3):
                        val = board[k+i][l+j]
                        gridseen[val] = 1 + gridseen.get(val, 0)
                        if val != "." and gridseen[val] > 1:
                            print(gridseen[val],i,j)
                            return False
        return True

        
        
        
