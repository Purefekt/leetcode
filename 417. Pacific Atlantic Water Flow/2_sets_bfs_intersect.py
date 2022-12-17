"""
Create 2 sets. All the cells which can flow into pacific ocean and all the cells which can flow into atlantic ocean
To create a set, for example pacific, add row 0 and col 0 to the pacific set
Then run bfs from all nodes of this set. For each node check in all 4 valid directions and add if the val of a child cell is <= to parent. This will mean the water can flow from child to parent
Result will be the intersection of these 2 sets

O(m*n) time to go over all cells. In the worst case, all cells flow to both ocean, in this case we will traverse all nodes twice, so 2*m*n
O(m*n) to store in visited and queue
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])

        # goal states would be row 0 and col 0 for pacific and row m-1 and col n-1 for atlantic
        pacific = set()
        atlantic = set()
        for j in range(n):
            pacific.add((0,j))
            atlantic.add((m-1,j))
        for i in range(m):
            pacific.add((i,0))
            atlantic.add((i,n-1))

        # run bfs from all goal states of both oceans. Go to only higher (not lower) levels. This way we will get 2 sets of cells which flow to either ocean
        pacific_queue = list(pacific)
        atlantic_queue = list(atlantic)

        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        while pacific_queue:
            node = pacific_queue.pop()
            r,c = node[0], node[1]
            for direction in directions:
                destination = tuple(map(lambda x,y:x+y, node, direction))
                new_r, new_c = destination[0], destination[1]
                if 0<=new_r<m and 0<=new_c<n and destination not in pacific and heights[r][c] <= heights[new_r][new_c]:
                    pacific.add(destination)
                    pacific_queue.append(destination)
        
        while atlantic_queue:
            node = atlantic_queue.pop()
            r,c = node[0], node[1]
            for direction in directions:
                destination = tuple(map(lambda x,y:x+y, node, direction))
                new_r, new_c = destination[0], destination[1]
                if 0<=new_r<m and 0<=new_c<n and destination not in atlantic and heights[r][c] <= heights[new_r][new_c]:
                    atlantic.add(destination)
                    atlantic_queue.append(destination)
        
        intersection_set = pacific.intersection(atlantic)

        return list(intersection_set)
