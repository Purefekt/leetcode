"""
Build a undirected graph.
A node can each all nodes in its own row and column.
So build 2 hashmaps, all nodes in a row and all nodes in a col.
Use these hashmaps to build the graph.
Run connected components algo on this graph, we can remove this many stones.

O(n) time where n is the number of stones since we travel to each node at most once.
O(n) space used by visited.
"""

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        # create hashmap of all points which exist in a row and a col
        row_map = collections.defaultdict(list)
        col_map = collections.defaultdict(list)
        for r,c in stones:
            row_map[r].append((r,c))
            col_map[c].append((r,c))

        # build an adj list
        adj = collections.defaultdict(set)
        for r,c in stones:
            adj[(r,c)] = adj[(r,c)].union(set(row_map[r]))
            adj[(r,c)] = adj[(r,c)].union(set(col_map[c]))
            adj[(r,c)].remove((r,c))
        
        # run connected components on this graph
        visited = set()
        components = 0
        for start in adj:
            if start in visited:
                continue
            components += 1
            stack = [start]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                for child in adj[node]:
                    if child not in visited:
                        stack.append(child)
                visited.add(node)
        
        return len(stones)-components