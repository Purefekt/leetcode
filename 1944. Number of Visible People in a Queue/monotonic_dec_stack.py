"""
Monotonic decreasing stack.
Do it from right to left.
Initialize res = [0] * n.
Go right to left, while top of stack < current height, keep popping and keep incrementing res[i] += 1.
Now if the stack is still not empty, add another 1 to res[i], since we can still see one more person to the right.
For example, after all popping the stack is [11], and our current height is 10. This means we can still see the person with height 11.

O(n) time to iterate through the array once.
On) space for the stack. 
"""

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(heights)

        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                res[i] += 1
            
            # add one more if stack exists since we can see atleast one more person to the right
            if stack:
                res[i] += 1
            
            stack.append(heights[i])
        
        return res
