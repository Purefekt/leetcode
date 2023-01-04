"""
Greedy. At a given point, we can calculate the number of open brackets on the left side since we traverse left to right
If we get a '(', then we increment by 1 and if we get a ')', then we decrement by 1
But if we get a '*', we can do either operation, so we keep 2 variables to keep a track of open brackets till that point, leftmax and leftmin
Whenever we see a '*', we will increment left_max by 1 and assume it is a '(', and decrement left_min by 1 and assume it is a s ')'.
If at any point left_max goes below 0, this means no matter what we do, this will never be a valid string
If at any point left_min goes below 0, we need to reset it to 0
In the end left_min must be 0 for it to be valid

O(n) time
O(1) space
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left_min = 0
        left_max = 0

        for c in s:
            if c == '(':
                left_min += 1
                left_max += 1
            elif c == ')':
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            
            # if left max ever becomes <0, for example in ()), this means no matter what we do, it will never be valid
            if left_max < 0:
                return False
            # reset left min if it becomes < 0, edge case (*)(
            if left_min < 0:
                left_min = 0
        
        if left_min == 0:
            return True
        return False
        