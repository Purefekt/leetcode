"""
Monotonic increasing stack.
Create a stack which takes a tuple (index it can stretch to on the left, height).
The first element in the tuple is the index which the current height can stretch to on the left side.
Due to the stack being increasing, we will keep elements in the stack till they can stretch to on the right side.
Before adding to the stack, remove all elements from the stack whose height is more than the current height.
Upon removal, get the max rectangle it can make and update the result. The length is the height of the popped element and the width is current index - popped index.
The index given to the element being added to the stack is the index of the last element which was popped.
If no elements were popped, ie the element at the top of the stack was smaller than the current element, then the left index will be current index.
Once all the elements are traversed, some might still be in the stack. Pop them and update result till stack is empty.
In this iteration, the right index will be len(heights) since all the remaining elements in the stack can stretch till the right end.

O(n) time since we add all elements and pop all elements from the stack once each, thus 2n.
O(n) space to hold at most n items in the stack.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0

        for i,h in enumerate(heights):
            if not stack:
                stack.append((i, h))
            else:
                # this is the index till the current bar can stretch to the left side
                left_idx = i
                while stack and h < stack[-1][1]:
                    old_i, old_h = stack.pop()
                    left_idx = old_i    
                    res = max(res, (i-old_i)*old_h)
                
                stack.append((left_idx, h))
        
        # get rectangle values from the remaining items in stack
        while stack:
            i, h = stack.pop()
            res = max(res, (len(heights)-i)*h)

        return res
