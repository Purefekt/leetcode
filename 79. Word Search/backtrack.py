"""
For every cell, run dfs and and find the word using backtracking
If any cell returns True, return True
Backtracking recursive func will take start row, start col and start index = 0
Return True if index == length of word
Return False if we go out of bounds or if that cell is visited or if the value in that board != word[index]

O(n * m * 3^l) time. Where m*n is the size of the grid. 3^l is the time taken by the backtracking function. at the first try we have 4 directions but after the first try we get 3 subsequent cells to go to since we cannot go back. Thus this is a 3-ary tree, the height of this tree will be the length l of the word.
O(l) space taken by the implicit stack
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        visited = set()

        def backtrack(r,c,idx):
            if idx == len(word):
                return True
            
            if r<0 or r>=m or c<0 or c>=n or (r,c) in visited or board[r][c] != word[idx]:
                return False
            
            # this is a valid cell so add it to visited
            visited.add((r,c))
            # explore all 4 directions
            res = backtrack(r+1,c,idx+1) or backtrack(r-1,c,idx+1) or backtrack(r,c+1,idx+1) or backtrack(r,c-1,idx+1)
            # backtrack
            visited.remove((r,c))
            return res
        
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0) is True:
                    return True
        return False
