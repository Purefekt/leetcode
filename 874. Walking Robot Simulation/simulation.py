"""
Simulate the movement.
Make 2 hashmaps for direction changes in left and right directions.
Convert obstacles to a set for quick checking.
For moving in a direction, run a loop till the amount.
If at any point, the next cell is an obstacle, stop that loop.

O(m+n) time where m is the size of commands and n is the size of obstacles since hashing obstacles require linear time. Commands takes O(9*m) time.
O(n) space to store obstacles set.
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set()
        for x,y in obstacles:
            obs.add((x,y))
        
        dir_change_right = {
            (-1,0): (0,1),
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1):(-1,0)
        }

        dir_change_left = {
            (-1,0): (0,-1),
            (0,-1): (1,0),
            (1,0): (0,1),
            (0,1): (-1,0)
        }

        cur = [0,0]
        cur_dir = (0,1)

        res = 0
        for c in commands:
            res = max(res, cur[0]**2 + cur[1]**2)
            if c == -1:
                cur_dir = dir_change_right[cur_dir]
            elif c == -2:
                cur_dir = dir_change_left[cur_dir]
            else:
                for _ in range(c):
                    next_cell = tuple(map(lambda x,y: x+y, cur, cur_dir))
                    if next_cell in obs:
                        continue
                    else:
                        cur = next_cell
        
        res = max(res, cur[0]**2 + cur[1]**2)
        return res
