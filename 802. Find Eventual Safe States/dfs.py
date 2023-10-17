"""
Recursively find the status of each node.
Create a hashmap safe_status and add only the nodes with 0 outgoing edges and set value to True.
Now for each node not in safe_status, run dfs.
During dfs, set the status of a node to False and then recursively run dfs on children.
If a child loops back to an ancestor, this ancestor will be present in safe_status hashmap with False value and thus return False.
The final status of a node will be AND of all its children. 
This way, we only need to compute once per each node.

O(v+e) time for dfs through all nodes and edges just once.
O(v) space for stack
"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        # identify initial safe nodes
        safe_status = {}
        for i in range(n):
            if len(graph[i]) == 0:
                safe_status[i] = True
        
        def dfs(node):
            if node in safe_status:
                return safe_status[node]
            
            # add this to safe_status = False
            safe_status[node] = False
            status = True
            for child in graph[node]:
                status = status and dfs(child)
            safe_status[node] = status
            return status


        for i in range(n):
            if i not in safe_status:
                dfs(i)
        
        # get all true vals
        res = []
        for i in range(n):
            if safe_status[i] is True:
                res.append(i)
        
        return res
