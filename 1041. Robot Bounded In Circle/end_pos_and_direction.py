"""
The robot will remain in a circle if after 1 iteration of the instruction, it follows these rules
1) it returns to the start state (0,0)
2) Even if it does not return to its start state, it is gauranteed to return to start if the ending direction of the instructions is not north. For example for GGLL, it takes 2 iterations to return to (0,0)
If the robot doesnt end at (0,0) in the first iteration and ends with its direction to north, it will always diverge away

O(n) time
O(1) space
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        directions_L = {
            (0,1):(-1,0),
            (1,0):(0,1),
            (0,-1):(1,0),
            (-1,0):(0,-1)
        }

        directions_R = {
            (0,1):(1,0),
            (1,0):(0,-1),
            (0,-1):(-1,0),
            (-1,0):(0,1)
        }

        start = (0,0)
        direction = (0,1)
        final_pos = (0,0)

        for c in instructions:
            if c=='G':
                final_pos = tuple(map(lambda x,y:x+y, final_pos, direction))
            elif c=='L':
                direction = directions_L[direction]
            else:
                direction = directions_R[direction]
        
        # if the final position doesnt change or if we end on a direction which is not north, we will remain in the circle
        if final_pos == (0,0):
            return True
        if direction != (0,1):
            return True
        return False
                