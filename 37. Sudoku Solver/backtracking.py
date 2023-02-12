"""
Backtracking
We need 3 hashmaps; row, col, subsection so that we dont build an invalid sudoku
Populate these 3 hashmaps with sets of all numbers which lie in them.
The subsection hashmap divides the board into 9 3x3 cells, we label them from 0-8 and use the encoding (i//3)*3 + (j//3) to put a cell (i,j) into [0,8]
Create a queue of all cell positions where there is an empty cell
Backtrack using the index of elements in the queue, base case is when idx == len(queue), return True
for each position queue[idx], we try to place numbers [1,9], to do this we check if its valid using the 3 hashmaps
If it is valid, then place the number on that board position, update the 3 hashmaps and backtrack to the next index.
We have 1 solution and we need to exit from the backtracking when we find one, thus we use Return True

O(9!^9) time. For each row we have 9! options and we create a tree with 9 as branching factor
O(1) space
"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        row_hashmap = {i:set() for i in range(9)}
        col_hashmap = {i:set() for i in range(9)}
        subsection_hashmap = {i:set() for i in range(9)}

        # add the initial sudoku to the hashmaps
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_hashmap[i].add(board[i][j])
                    col_hashmap[j].add(board[i][j])
                    subsection_hashmap[(i//3)*3 + (j//3)].add(board[i][j])
        
        # get all spaces where we can add a number
        queue = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    queue.append((i,j))
        
        def backtrack(idx):
            if idx == len(queue):
                return True
            
            r,c = queue[idx]
            
            for i in range(1,10):
                i = str(i)
                if i not in row_hashmap[r] and i not in col_hashmap[c] and i not in subsection_hashmap[(r//3)*3 + (c//3)]:

                    board[r][c] = i
                    row_hashmap[r].add(i)
                    col_hashmap[c].add(i)
                    subsection_hashmap[(r//3)*3 + (c//3)].add(i)

                    if backtrack(idx+1) is True:
                        return True
                    
                    board[r][c] = '.'
                    row_hashmap[r].remove(i)
                    col_hashmap[c].remove(i)
                    subsection_hashmap[(r//3)*3 + (c//3)].remove(i)
            
            return False
        
        backtrack(0)
            