"""
Build the adj list one by one by adding the edges. Since this is bidirectional add src->dst and also dst->src
After updating the adj list with an edge, run dfs in undirected graph to check for cycles.
Start with the stack with [(src, None)] where src is the start node and None is its parent
For each child, if the child is NOT the parent and it has been visited, this means there is a cycle, return False
Otherwise if the child hasnt been visited, then add it to the stack and mark the node as visited

O(n^2) since we build the adj list for num of edges which is equal to number of nodes. Each iteration of dfs is O(n+e) but n==e
O(n) to maintain adj list of number of edges

"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj = {i:[] for i in range(1,len(edges)+1)}
        
        def dfs_to_check_cycle(start):
            stack = [(start, None)]
            visited = set()
            while stack:
                node, parent = stack.pop()
                for child in adj[node]:
                    if child != parent and child in visited:
                        return False
                    if child not in visited:
                        stack.append((child, node))
                visited.add(node)
            return True


        # build the adj list one by one and run dfs each time, when there is a cycle, we return that edge
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

            if dfs_to_check_cycle(src) is False:
                return [src, dst]
