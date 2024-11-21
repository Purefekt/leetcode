"""
Brute force.
For each guard, try all directions.
Stop when we hit a wall or a guard.

O(m*n) time.
O(m*n) space.
"""

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        # get all locations which are locked
        blocked = set([(a,b) for a,b in guards])
        for a,b in walls:
            blocked.add((a,b))
        
        walls = set([(a,b) for a,b in walls])
        guards = set([(a,b) for a,b in guards])
        
        for i,j in guards:
            x,y = i,j
            while x+1<m and (x+1,j) not in walls and (x+1,j) not in guards:
                blocked.add((x+1,y))
                x += 1
            
            x,y = i,j
            while y+1<n and (x,y+1) not in walls and (x,y+1) not in guards:
                blocked.add((x,y+1))
                y += 1
            
            x,y = i,j
            while x-1>=0 and (x-1,y) not in walls and (x-1,y) not in guards:
                blocked.add((x-1,y))
                x -= 1
            
            x,y = i,j
            while y-1>=0 and (x,y-1) not in walls and (x,y-1) not in guards:
                blocked.add((x,y-1))
                y -= 1

        return (m*n) - len(blocked)
