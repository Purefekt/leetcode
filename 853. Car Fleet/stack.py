"""
The car closest to the target needs (target-position)/speed time to reach it.
The car just behind it also needs the same for its own position and speed.
if the 2nd car needs less time to reach the end, this means it will merge with the car in front of it before both reach the end
We create a 2d list of speed_pos and sort by position.
We create a stack and add the last car (closest to target) to the stack, [position, speed, time till finish]
We run a loop from the right side to the left, for each car we check its time till finish, if its time is <= the car in front of it (top most in stack), then we dont add this car to the stack
If its time to reach end is more than the car in front of it, means it will never merge and we add it to the stack

O(nlogn) for sorting
O(n) to hold in stack
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        speed_pos = []
        for i in range(len(position)):
            speed_pos.append([position[i], speed[i]])
        speed_pos.sort()

        # add the pos, speed and time taken to reach target in the stack. Start with the last car, the most ahead
        time_taken_last_car = (target - speed_pos[-1][0])/speed_pos[-1][1]
        
        stack = [[speed_pos[-1][0], speed_pos[-1][1], time_taken_last_car]]

        for i in range(len(speed_pos)-2, -1, -1):
            time_taken_this_car = (target - speed_pos[i][0])/speed_pos[i][1]
            if time_taken_this_car > stack[-1][2]:
                stack.append([speed_pos[i][0], speed_pos[i][1], time_taken_this_car])

        return len(stack)
