"""
Use bfs to go through all nodes from the start node and build an adj list of their vals since all node vals are unique
Go through the keys of the adj list and make new nodes using the Node class. Also make a lookup table from node vals to new nodes
Go through the adj list and based on the child vals and lookup table populate the children of the new nodes

O(m+n) time where n is number of nodes and m is number of edges.
O(n) space to store n number of nodes in visited
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None

        adj = {}
        queue = [node]
        visited = set()

        while queue:
            cur_node = queue.pop(0)
            adj[cur_node.val] = []
            for child in cur_node.neighbors:
                adj[cur_node.val].append(child.val)
                if child not in visited:
                    queue.append(child)
            
            visited.add(cur_node)
        
        # build new nodes
        val_to_node = {}
        for k in adj.keys():
            new_node = Node(k,[])
            val_to_node[k] = new_node
        
        
        # add to the new nodes
        for k in adj.keys():
            for child_vals in adj[k]:
                val_to_node[k].neighbors.append(val_to_node[child_vals])
        
        return val_to_node[1]
