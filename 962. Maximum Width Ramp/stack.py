"""
Two pass with monotonic dec stack.
Create a stack from iterating left to right but only in decreasing num.
So for [6,0,8,2,1,5], our stack will be [6,0].
Keep indices for easy use.
Then run another pass by iterating right to left.
For each num, if the top of stack if <= to this num, then we can use their distance as the result.
Keep popping and analyzing against top of stack before moving to the next num.
Once stack is empty, break out.

O(n) time for two passes over nums.
O(n) space used by stack.
"""

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        # create dec stack
        stack = []
        for i,n in enumerate(nums):
            if not stack:
                stack.append(i)
            else:
                if nums[stack[-1]] > n:
                    stack.append(i)

        # iterate from right end to find valid pairs
        res = 0
        for i in range(len(nums)-1, -1, -1):
            if not stack:
                break
            while stack and nums[stack[-1]] <= nums[i]:
                res = max(res, i-stack[-1])
                stack.pop()
        
        return res
