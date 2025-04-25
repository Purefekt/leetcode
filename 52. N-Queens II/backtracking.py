"""
Backtracking.
Recursive function takes row index and visited set.
row index is the row in which we are trying to place a queen.
Once we place a queen at a cell which has not been visited, we add new unusable cells.
These cells are the same row, same column and both diagnols.
Keep track of just the new unusable cells introduced since some cells which become unusable due to adding this queen might already be in the visited set.
Backtrack by removing JUST the cells which were newly added due to placing a queen at current cell.

O(n!) time since we first have n possible positions for a queen, when we place it, this removes 1 col and 1 diagnol in the next row leaving us with n-2 options and so on.
O(n^2) space used by visited set since board size is n*n.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def backtrack(idx, visited):
            if idx == n:
                return 1
            
            res = 0
            # try to place a queen at each col in idx row
            for j in range(n):
                if (idx, j) not in visited:
                    # once we add a queen, get all the spots that become unusable
                    unusable = set()
                    # same row
                    for col in range(n):
                        unusable.add((idx, col))
                    # same col
                    for row in range(n):
                        unusable.add((row, j))
                    # right up diagnol
                    row = idx
                    col = j
                    while row >= 0 and col < n:
                        unusable.add((row,col))
                        row -= 1
                        col += 1
                    # right down diagnol
                    row = idx
                    col = j
                    while row < n and col < n:
                        unusable.add((row,col))
                        row += 1
                        col += 1
                    # left up diagnol
                    row = idx
                    col = j
                    while row >= 0 and col >= 0:
                        unusable.add((row, col))
                        row -= 1
                        col -= 1
                    # left down diagnol
                    row = idx
                    col = j
                    while row < n and col >= 0:
                        unusable.add((row, col))
                        row += 1
                        col -= 1
                    
                    # get the unique cells that will be added as a result of this cell being chosen
                    new_unusable = unusable - visited
                    visited = visited.union(new_unusable)
                    res += backtrack(idx+1, visited)
                    visited = visited - new_unusable
            
            return res
        
        return backtrack(0, set())
