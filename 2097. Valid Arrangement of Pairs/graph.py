"""
Treat each number in pairs as a node.
So [a,b], we have 2 nodes of a graph: a and b.
For each pair, create an adj list and also track the in deg and out degree of each node.
Since we are gauranteed a path, there will be one node which has out degree = in degree + 1.
And if no such node exists, then we can simply start with the first node.
Once the first node is identified, we postorder dfs traverse it and the resultant path will be the reverse of the solution path.
Reverse this path which will look like: [a,b,c,d,e,f].
Use this to build the result with adjacent nodes => [(a,b), (b,c), (c,d), (d,e), (e,f)]

O(v+n) time where we have v nodes and n edges (same as input pairs size). Build adj list takes e time, finding start node takes v time. Dfs takes e time and reversing takes v time.
O(v+e) space for adj list, in degree, out degree and stack.
"""

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        
        adj = collections.defaultdict(deque)
        in_deg = collections.defaultdict(int)
        out_deg = collections.defaultdict(int)

        for a,b in pairs:
            adj[a].append(b)
            in_deg[b] += 1
            out_deg[a] += 1
        
        # find starting
        start = pairs[0][0]
        for k in out_deg:
            if out_deg[k] == in_deg[k] + 1:
                start = k
                break
        
        # traverse postorder dfs
        path = []
        def postorder(node):
            while adj[node]:
                child = adj[node].popleft()
                postorder(child)
            path.append(node)
        postorder(start)

        path = path[::-1]

        # build result pairs
        out = []
        for i in range(len(path)-1):
            out.append([path[i], path[i+1]])
        return out
