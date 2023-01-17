"""
Use a stack and simulate the collisions left to right. If the stack is empty add the asteroid. (In the first go always add the first asteroid)
If the asteroid is positive, add to the stack without any condition
Next if the asteroid is negative (moving left) and the previous asteroid is also negative, simply add to stack since they will never meet
Else if the asteroid is negative and the previous asteroid is positive, this means there is a collision, pop asteroids if they are smaller than the current asteroid
Finally check if the current asteroid and last of the remaining asteroids is equal to it, if equal then pop and dont add to the stack
If the last of the remaining asteroids is larger than the current asteroid, do nothing. If there are no remaining asteroids then add the current asteroid to the stack

O(n) time to go through all asteroids atleast once
O(n) space to maintain the stack
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
            else:
                if asteroids[i] < 0:
                    if stack[-1] < 0:
                        stack.append(asteroids[i])
                    else:
                        while stack and abs(asteroids[i]) > stack[-1] and stack[-1] > 0:
                            stack.pop()
                        if stack and abs(asteroids[i]) == stack[-1]:
                            stack.pop()
                        elif stack and abs(asteroids[i]) < stack[-1]:
                            continue
                        else:
                            stack.append(asteroids[i])

                else:
                    stack.append(asteroids[i])
        
        return stack
        