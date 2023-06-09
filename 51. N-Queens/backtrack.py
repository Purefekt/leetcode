"""
Backtracking
Each row can only have a single queen
Place a queen at a position in a row, then go to the next row and try to place a queen
When we place a queen, the column also gets locked
The positive diagnol and the negative diagnols also get locked
Thus track where the queen have been placed, current row, locked columns, locked positive diagnol cells, locked negative diagnol cells.

O(n!) time. When placing the first queen we have n options. this cancels one column and one diagnol for the queen in the next row, she gets n-2 options and so on.
O(n^2) space to store the 3 sets and recursion stack since the board size is n*n
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # every row can only have 1 queen
        # once we put the queen at a place, that column is locked
        # the positive diagnol and negative diagnols are also locked

        pos_diag = [(1,-1), (-1,1)]
        neg_diag = [(-1,-1), (1,1)]

        res = []
        def backtrack(queen_positions, r, locked_col, locked_pos_d, locked_neg_d):
            # if we complete all rows, means we got a valid solution
            if r == n:
                res.append(queen_positions.copy())
                return

            for c in range(n):
                # place the queen at a valid position in the current row
                if c not in locked_col and (r,c) not in locked_pos_d and (r,c) not in locked_neg_d:
                    queen_positions.append((r,c))
                
                    # lock that column
                    locked_col.add(c)

                    # lock both diags as well. Expand the diagnol with the point in the middle. Adding negative points is fine
                    to_add_pos_d = set()
                    for k in range(1,n):
                        for d in pos_diag:
                            dest = tuple(map(lambda x,y: (x*k)+y, d, (r,c)))
                            to_add_pos_d.add(dest)
                    locked_pos_d = locked_pos_d.union(to_add_pos_d)

                    to_add_neg_d = set()
                    for k in range(1,n):
                        for d in neg_diag:
                            dest = tuple(map(lambda x,y: (x*k)+y, d, (r,c)))
                            to_add_neg_d.add(dest)
                    locked_neg_d = locked_neg_d.union(to_add_neg_d)

                    backtrack(queen_positions, r+1, locked_col, locked_pos_d, locked_neg_d)

                    # backtrack
                    queen_positions.pop()
                    locked_col.remove(c)
                    locked_pos_d -= to_add_pos_d
                    locked_neg_d -= to_add_neg_d
            
            return
        
        backtrack([], 0, set(), set(), set())

        # build the board using the queen postions in the valid sol
        solution = []

        for combo in res:
            this_combo = []
            for i in range(n):
                this_str = ""
                for j in range(n):
                    if combo[i][1] == j:
                        this_str += "Q"
                    else:
                        this_str += "."
                this_combo.append(this_str)
            solution.append(this_combo)
        
        return solution
