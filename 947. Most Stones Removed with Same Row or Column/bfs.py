"""
BFS, find number of graphs. For the given points we need to find the number of disjoint graphs
We first create an adjacency list of all nodes to to a list of all nodes with same x or y coordinate
Then we find the number of graphs bt iterating over all stones and running bfs from each. 
For each bfs run we increment the number of graphs by 1 and keep adding all nodes to visited to avoid rechecking them.

O(n^2 + e) time. Building the adj list rakes O(n^2) time. e is the number of edges, there can be at max e = n*(n-1) edges when all stones are connected to each other. Building the graph takes O(n) time since we visit each node once and mark it as visited. We iterate over the edge list of each stone which take e time.
O(n+e) space. The adj list takes e space since it contains a list of all edges. The visited set stoes all nodes and takes n space.
"""

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        adj = {}
        for stone in stones:
            adj[tuple(stone)] = []

        for stone in stones:
            this_stone = tuple(stone)
            for stone in stones:
                stone = tuple(stone)
                if this_stone != stone:
                    if this_stone[0] == stone[0] or this_stone[1] == stone[1]:
                        adj[this_stone].append(stone)

        # find number of graphs
        num_graphs = 0
        visited = set()
        for node in adj.keys():
            if node not in visited:
                num_graphs += 1
                # run bfs starting this node and add all its children to visited
                queue = [node]
                while queue:
                    curr_node = queue.pop(0)
                    for child in adj[curr_node]:
                        if child not in visited:
                            queue.append(child)
                    visited.add(curr_node)

        # we can keep 1 stone from each graph + num lone stones remain. Res = total - num graphs - num lone
        return len(stones) - num_graphs
        