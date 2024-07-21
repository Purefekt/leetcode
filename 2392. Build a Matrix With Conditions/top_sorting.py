"""
Topological sorting.
Think of the relationships of conditions as edges.
Treat both row and cols as separate till the end and use them to get the position in 2d matrix.
Do the following for both conditions:
Build adj list.
Run topological sorting algo, is an order cannot be made, return [].
If both kinds of orders can be made, use the row order to get the ith position in matrix.
And use the col order to get the jth position in matrix.

O(max(k^2, n)) time. Topological sorting takes n time. To fill the matrix it takes k*k time.
O(max(k^2, n)) space. Topological sorting queue takes n time and matrix takes k*k space.
"""

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        # build adj list, in degree map and started queue for topological sorting
        def build_adj(cond, k):
            adj = {i:set() for i in range(1, k+1)}
            in_deg = {i:0 for i in range(1, k+1)}
            # do not use duplicate edges
            seen_edge = set()
            for a,b in cond:
                if (a,b) in seen_edge:
                    continue
                adj[a].add(b)
                in_deg[b] += 1
                seen_edge.add((a,b))
            queue = []
            for k,v in in_deg.items():
                if v == 0:
                    queue.append(k)
            return adj, in_deg, queue
        
        adj_row, in_deg_row, queue_row = build_adj(rowConditions, k)
        adj_col, in_deg_col, queue_col = build_adj(colConditions, k)
        
        # get topological sorting order for both
        def top_sort(queue, adj, in_deg):
            res = []
            while queue:
                node = queue.pop(0)
                res.append(node)
                for child in adj[node]:
                    in_deg[child] -= 1
                    if in_deg[child] <= 0:
                        queue.append(child)
            status = True
            for v in in_deg.values():
                if v > 0:
                    status = False
                    break
            
            return res, status
        
        ordering_row, status_row = top_sort(queue_row, adj_row, in_deg_row)
        ordering_col, status_col = top_sort(queue_col, adj_col, in_deg_col)

        if not status_row or not status_col:
            return []

        # get cell values for each number
        res = []
        for i in range(k):
            res_row = []
            for j in range(k):
                res_row.append(0)
            res.append(res_row)
        
        pos = {i:[0,0] for i in range(1, k+1)}

        for i in range(len(ordering_row)):
            pos[ordering_row[i]][0] = i
        for j in range(len(ordering_col)):
            pos[ordering_col[j]][1] = j
        
        # place in their positions
        for k,v in pos.items():
            res[v[0]][v[1]] = k
        
        return res
