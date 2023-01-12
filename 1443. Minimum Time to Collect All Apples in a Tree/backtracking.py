"""
We calculate the amount of time taken at each subtree.
Using backtracking, we can send the data to parent nodes. 
Our recursive function will have node and parent passed to avoid going back to the parent from a child

O(n) time for n number of nodes
O(n) space to store the adj list and implicit stack 
"""

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        # build adj list
        adj = {i:[] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        def dfs(node, parent):
            time = 0

            for child in adj[node]:
                if child == parent:
                    continue
                
                # this is the time it took for the subtree rooted at child
                child_time = dfs(child, node)
                
                # Add the child time and the time it takes to go and come back to that subtree
                if child_time or hasApple[child]:
                    time += 2+ child_time

            return time
        
        return dfs(0, None)
