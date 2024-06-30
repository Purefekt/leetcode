"""
Hard problem. See note pdf.
O(v+e) time for multiple passes over the entire graph.
O(v+e) for multple adj lists
"""

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        # create graph with just type 3 edges
        adj_both = {i:[] for i in range(1, n+1)}
        for t,u,v in edges:
            if t == 3:
                adj_both[u].append(v)
                adj_both[v].append(u)
        # get components in this graph and also map a node to a component. Also track the total number of edges needed ie sum(size of component - 1) since minimum edges needed to make a component = n-1.
        edges_needed = 0
        node_to_com = {}
        visited = set()
        com = 0
        for i in range(1, n+1):
            if i not in visited:
                com += 1
                size_of_com = 0
                # start dfs
                stack = [i]
                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    size_of_com += 1
                    node_to_com[node] = com
                    for child in adj_both[node]:
                        stack.append(child)
                    visited.add(node)
                edges_needed += (size_of_com - 1)
        
        # consider a component as a node. Now build graph for Alice by using components as nodes. For each edge in Alice's type, get the component that node is in.
        # If both nodes of the edge are in the same component, then skip this edge since it wont help.
        adj_alice = {i:[] for i in range(1, com+1)}
        for t,u,v in edges:
            if t == 1:
                u = node_to_com[u]
                v = node_to_com[v]
                if u!=v:
                    adj_alice[u].append(v)
                    adj_alice[v].append(u)
        # Run connected components on alice's graph. If there are >1 components, return -1.
        com_alice = 0
        visited = set()
        for i in range(1, com+1):
            if i not in visited:
                com_alice += 1
                stack = [i]
                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    for child in adj_alice[node]:
                        stack.append(child)
                    visited.add(node)
        if com_alice > 1:
            return -1
        
        # Repeat for Bob
        adj_bob = {i:[] for i in range(1, com+1)}
        for t,u,v in edges:
            if t == 2:
                u = node_to_com[u]
                v = node_to_com[v]
                if u!=v:
                    adj_bob[u].append(v)
                    adj_bob[v].append(u)
        # Run connected components
        com_bob = 0
        visited = set()
        for i in range(1, com+1):
            if i not in visited:
                com_bob += 1
                stack = [i]
                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    for child in adj_bob[node]:
                        stack.append(child)
                    visited.add(node)
        if com_bob > 1:
            return -1
        
        # Now we are guaranteed that both Alice and Bob have only 1 connected component
        # Add 2 * (com-1) to edges needed since we add the edges needed by both Alice and Bob to traverse the graph in the least number of edges
        edges_needed += (2 * (com-1))

        # return total edges - edges actually needed
        return len(edges) - edges_needed
