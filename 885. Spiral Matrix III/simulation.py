"""
Simulation.
The distance travelled in each direction has a pattern.
1,1,2,2,3,3,4,4,5,5,6,6,...
After moving x amount of distance, we change direction in a known manner.
Run a while loop till the result size == rows * cols ie we have included all spots of the grid into the result.
Start at rStart, cStart and move that number of steps in current direction.
Assume we are on an infinite plane, but only add the cells which fall within the boundary.
This boundary is 0 <= r < rows and 0 <= c < cols.
Update the step size every 2 iterations.

O(max(rows, cols)^2) time since we might move outside of the boundary.
O(rows * cols) time used by res. But if we dont count it, no additional memory was used.
"""

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        # the number of steps in a dir is 1,1,2,2,3,3,4,4,5,5,6,6,etc
        dir_change = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1, 0),
            (-1,0): (0,1)
        }
        step = 1
        factor = 0
        cur = [rStart, cStart]
        res = [cur]
        direction = (0,1)
        while len(res) < rows * cols:
            for i in range(step):
                cur = [cur[0]+direction[0], cur[1]+direction[1]]
                # add this to res if it is valid
                if cur[0] >= 0 and cur[1] >= 0 and cur[0]<rows and cur[1]<cols:
                    res.append(cur)
            # change direction
            direction = dir_change[direction]

            factor += 1
            if factor == 2:
                step += 1
                factor = 0

        return res