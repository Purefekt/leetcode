"""
Monotonic increasing stack.
We create a stack where each element is the largest number in a given chunk.
Iterate over the array.
If a number is larger than the top element, this means we can start a new chunk with this number, so place it at the top of the stack.
If the number is smaller, pop all elements larger than current number.
All these numbers will form the chunk. Take the max of these and place them at the top of stack.

O(n) time since even though we use max function within a loop, we only ever search n times since the array in which we find the max can only have a number added to it at max once.
O(n) space used by stack.
"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        stack = []

        for n in arr:
            cur = [n]
            while stack and stack[-1] > n:
                cur.append(stack.pop())
            # push the max num from this stack back 
            stack.append(max(cur))
        
        return len(stack)
