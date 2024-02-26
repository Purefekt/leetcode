"""
This is a graph prolem.
If a/b = 2, then there is an edge between node a -> b with a weight of 2.
And there is an edge between b -> a with a weight of 1/2.
These weights wont be added but instead it will be multiplied.
Create the adj list where keys are the nodes and values are (child, weight).
For each query, if either 1 or both are not in the adj list, then append -1 since these nodes do not exist.
If they exist, simply run dfs from src to dst. Track the current value, begin with 1 and each time we use an edge, multiply that to the weight.
Return the val if we reach the dst. If we cannot reach the dst, append -1.

O(m*n) time where we have n equations and m queries. To build graph we need to run in n time, for each query we run dfs which can run for n time. Thus we get m*n time.
O(n) space used by the adj list, n space used by the stack and n space used by the visited set.
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = collections.defaultdict(list)
        for i in range(len(equations)):
            a,b = equations[i]
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))

        def dfs(src, dst):
            stack = [(src, 1)]
            visited = set()
            while stack:
                node, val = stack.pop()
                if node in visited:
                    continue
                if node == dst:
                    return val
                for child, child_multiplier in adj[node]:
                    stack.append((child, val*child_multiplier))
                visited.add(node)
            
        
        res = []
        for src, dst in queries:
            if src not in adj or dst not in adj:
                res.append(-1.0)
            else:
                # run dfs
                val = dfs(src, dst)
                if not val:
                    res.append(-1.0)
                else:
                    res.append(val)
        
        return res
