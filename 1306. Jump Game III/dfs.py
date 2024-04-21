"""
DFS.
Initialize stack with [start].
If the arr[node] is 0, return True.
Check if we can travel left ie we are >= 0 and then add this to stack.
Check if we can travel right ie we are < len(arr) and then add this to stack.

O(n) time to go through all nodes at most once.
O(n) used by stack and visited set.
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if arr[node] == 0:
                return True
            
            if node in visited:
                continue
            
            # check if left and right are possible
            if node - arr[node] >= 0:
                stack.append(node - arr[node])
            if node + arr[node] < len(arr):
                stack.append(node + arr[node])
            
            visited.add(node)
        
        return False
