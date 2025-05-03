"""
Modified Dijkstras.
Instead of min distance, track min absolute difference.
We place (min abs diff, node) into the pq.
Pop the diff, node from the pq.
We add the max(diff, new diff) to the pq.
new diff is the abs diff between node and its child.

O(m*n*log(m*n)) time. m*n number of nodes and for each node, we push and pop from heap once which takes log(m*n) time.
O(m*n) space used by min diff hashmap and queue.
"""

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        # dijkstras but edge weights are the abs diff and store the min distance in terms of min abs diff
        m,n = len(heights), len(heights[0])

        min_diff = {}
        for i in range(m):
            for j in range(n):
                min_diff[(i,j)] = math.inf
        
        pq = [(0, (0,0))]
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while pq:
            diff, node = heapq.heappop(pq)
            if node in visited:
                continue
            min_diff[node] = diff

            for d in directions:
                dest = tuple(map(lambda x,y: x+y, node, d))
                r,c = dest
                if 0<=r<m and 0<=c<n and dest not in visited:
                    new_diff = abs(heights[node[0]][node[1]] - heights[r][c])
                    if new_diff < min_diff[dest]:
                        heapq.heappush(pq, (max(diff, new_diff), dest))
            visited.add(node)
        
        return min_diff[(m-1, n-1)]
