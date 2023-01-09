"""
BFS, go through the board, when we get a cell with 'O', run bfs in 4 directions and get a given regions. This way get a list of all regions.
Next go through all points in all regions and see if that region is valid. A region is invalid if ANY point in it lies on the first row and col or the last row and col
Filter and get valid regions. Now go through all points in all valid regions and flip them to 'X'

O(m*n) time. One pass to get regions, one pass to filter regions and one pass to flip regions
O(m*n) space to store the valid cells. In the worst case all cells except the ones in first and last row and col are valid. Our list will contain (m-1)*(n-1) elements
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        # get all regions in the board
        regions = []
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    queue = [(i,j)]
                    current_region = [(i,j)]
                    visited.add((i,j))
                    while queue:
                        node = queue.pop(0)

                        for direction in directions:
                            dest = tuple(map(lambda x,y:x+y, node, direction))
                            r,c = dest

                            if dest not in visited and 0<=r<m and 0<=c<n and board[r][c] == 'O':
                                queue.append((r,c))
                                current_region.append((r,c))
                                visited.add((r,c))
                    regions.append(current_region)
        
        # get the valid regions by removing regions which contain cells in the first, last row and col
        def get_valid_regions(region):
            for cell in region:
                i,j = cell
                if 0 in cell:
                    return False
                if i == m-1 or j == n-1:
                    return False
            return True
        
        valid_regions = []
        for region in regions:
            if get_valid_regions(region) is True:
                valid_regions.append(region)
        
        # for all cells in the valid region, make then 'X'
        for region in valid_regions:
            for i,j in region:
                board[i][j] = 'X'
        