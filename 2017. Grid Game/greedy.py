"""
Greedy with a twist.
Robot1 doesnt move in a way to maximize its own points, but it moves in a way to MINIMIZE robot2's points.
A robot can only go right and then down only once. When it moves this way, it splits the board into top and bottom.
So when robot2 will travel, it will have to choose between either top row or bottom row, based on the max sum.
Find the index at which robot1 goes down by taking the path with the least of sum(top) and sum(bot)

O(n) time to traverse the top and bottom rows over multiple passes.
O(n) space for prefixsum arrays
"""

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])

        # calculate prefixsums for easy calculation
        psum1 = [grid[0][0]]
        for i in range(1, n):
            psum1.append(psum1[i-1] + grid[0][i])
        psum2 = [grid[1][0]]
        for i in range(1, n):
            psum2.append(psum2[i-1] + grid[1][i])
        
        # optimal for robot1 is to take path with least left for robot 2
        # check for every inex where robot1 can go down
        down_idx = 0
        min_left = math.inf
        for i in range(n):
            if i == 0:
                top = psum1[n-1] - psum1[i]
                bot = 0
            elif i == n-1:
                top = 0
                bot = psum2[i-1]
            else:
                top = psum1[n-1] - psum1[i]
                bot = psum2[i-1]
            max_val = max(top, bot)
            if max_val < min_left:
                min_left = max_val
                down_idx = i
        
        # update grid by setting 0s on robot1's path
        for i in range(down_idx+1):
            grid[0][i] = 0
        for i in range(down_idx, n):
            grid[1][i] = 0
        
        # robot2's optimal path is the row with higher sum
        return max(sum(grid[0]), sum(grid[1]))
