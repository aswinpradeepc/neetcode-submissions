class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in seen:
                    return False
                seen.add(board[i][j])

            seenv = set()
            for j in range(9):
                if board[j][i] != "." and board[j][i] in seenv:
                    return False
                seenv.add(board[j][i])

        for i in range(0,9,3):
            for j in range(0,9,3):
                hehe = set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        print(k,l)
                        if board[k][l] in hehe:
                            print(k,l,"lastset")
                            return False
                        if board[k][l] != ".":
                            hehe.add(board[k][l])
        return True
