"""
We need to track the number of extra closing brackets we have while iterating over the array.
We will use this to get the max number of extra closing brackets we had during this iteration.
The result is actually math.ceil(max_closing/2), this is because each swap will get rid of 2 brackets for us.
For example -> ]]][[[, here we get 3 as max closing, this means 2 swaps will take care of it.

O(n) time to iterate over the input once.
O(1) space to store max_closing and closing.
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        
        max_closing = 0
        closing = 0

        for c in s:
            if c == ']':
                closing += 1
                max_closing = max(max_closing, closing)
            else:
                closing -= 1
        
        return math.ceil(max_closing/2)
