"""
BFS
Run bfs and keep a track of visited.
At the end if we have all rooms in visited ie the len of visited is same as number of rooms, we visited all, else False

O(e+v) time for bfs
O(n) space to store the adj list
"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # build adj list
        adj = {i:rooms[i] for i in range(len(rooms))}
        
        queue = [0]
        visited = set()

        while queue:
            node = queue.pop(0)
            for child in adj[node]:
                if child not in visited:
                    queue.append(child)
            visited.add(node)
        
        if len(visited) != len(rooms):
            return False
        return True
