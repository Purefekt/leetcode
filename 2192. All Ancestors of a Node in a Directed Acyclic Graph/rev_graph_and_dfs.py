"""
Reverse graph and cache dfs.
Reverse the graph and run dfs from any node.
While dfs in a reversed graph, we can add the child (actually parent) of a node to its ancestor set.
Cache this so that if we encounter a node already explored, we can just add all of its parents to the current node's ancestor set.

O(v+eloge) time since the creation of rev adj list takes v+e time and the dfs runs at max v+e times since caching. We sort in the end of eloge time as well.
O(v+e) space used by adj list.
"""

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        # create rev edges adj list
        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[b].append(a)
        
        cache = {}
        def dfs(node):
            if node in cache:
                return cache[node]
            
            res = set()
            for child in adj[node]:
                res.add(child)
                res = res.union(dfs(child))
            cache[node] = res
            return res

        # start dfs from any node and use cache
        for i in range(n):
            dfs(i)
        
        output = []
        for i in range(n):
            output.append(sorted(list(cache[i])))
        
        return output
            