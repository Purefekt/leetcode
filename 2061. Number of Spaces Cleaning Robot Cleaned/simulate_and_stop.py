"""
Simulate the robots behavior.
Stop when we reach a cell which is already cleaned and the direction is the same as well.
So maintain a seen set where each element is a tuple (cur[0], cur[1], direction[0], direction[1]).

O(m*n) time since we can go over all cells at most once.
O(4*m*n) space used by the seen set.
"""

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        
        m = len(room)
        n = len(room[0])
        changes = {
            (0,1):(1,0),
            (1,0):(0,-1),
            (0,-1):(-1,0),
            (-1,0):(0,1)
        }

        cur = (0,0)
        direction = (0,1)
        seen = set()
        while True:
            # mark current as cleaned
            i,j = cur
            room[i][j] = 2
            seen.add((cur[0], cur[1], direction[0], direction[1]))
            rotations = 0
            while True:
                if rotations == 4:
                    break
                next_cell = tuple(map(lambda x,y: x+y, cur, direction))
                r,c = next_cell
                if 0<=r<m and 0<=c<n and room[r][c] == 2:
                    if (r,c, direction[0], direction[1]) in seen:
                        rotations = 4
                        break
                    else:
                        cur = next_cell
                        break
                if 0<=r<m and 0<=c<n and room[r][c] == 0:
                    cur = next_cell
                    break
                else:
                    rotations += 1
                    direction = changes[direction]
            if rotations == 4:
                break

        for row in room:
            print(row)
        # count number of 2s
        res = 0
        for i in range(m):
            for j in range(n):
                if room[i][j] == 2:
                    res += 1
        
        return res
