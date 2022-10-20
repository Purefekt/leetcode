"""
Check for each row, col and submatrix using hashset
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check the row
        for i in range(len(board)):
            hashset = set()
            for j in range(len(board[0])):
                if not board[i][j].isnumeric():
                    continue
                elif board[i][j] not in hashset and board[i][j].isnumeric():
                    hashset.add(board[i][j])
                else:
                    return False
        
        # check column
        for i in range(len(board)):
            hashset = set()
            for j in range(len(board[0])):
                if not board[j][i].isnumeric():
                    continue
                elif board[j][i] not in hashset and board[j][i].isnumeric():
                    hashset.add(board[j][i])
                else:
                    return False
        
        # check 3x3 subcolumn
        starting_points = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for r,c in starting_points:
            hashset = set()
            for i in range(3):
                for j in range(3):
                    if not board[r+i][c+j].isnumeric():
                        continue
                    elif board[r+i][c+j] not in hashset and board[r+i][c+j].isnumeric():
                        hashset.add(board[r+i][c+j])
                    else:
                        return False
        
        return True
                    