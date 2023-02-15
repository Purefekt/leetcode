"""
DFS with memoization
We need to run dfs from each cell and get the max path from that cell
To get the max path from a cell, it is itself a path of size 1 so res=1 at first. Then we need to get the max path from all 4 of its neighbors recursively. Need to check validity of a path if its in bounds and if its larger than its parent
Add the max path from the 4 neighbors of a cell to its res and return
Using memoization we only need to compute the paths once for each cell 

O(m*n) time to go over all cells once
O(m*n) space, the size of the implicit stack
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        memo = {}

        def dfs(r,c):

            if (r,c) in memo:
                return memo[(r,c)]

            res = 1

            max_path = 0
            for direction in directions:
                destination = tuple(map(lambda x,y:x+y, direction, (r,c)))
                new_r, new_c = destination

                if 0<=new_r<m and 0<=new_c<n and matrix[new_r][new_c] > matrix[r][c]:
                    max_path = max(max_path, dfs(new_r, new_c))
            
            res += max_path
            memo[(r,c)] = res
            return res
        
        for i in range(m):
            for j in range(n):
                dfs(i,j)
        
        return max(memo.values())
