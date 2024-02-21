"""
Bit manipulation.
We only need to get the common bits in left and right, since the middle numbers dont really matter due to property of AND.
We need to reduce left and right to make it same, this will give us the common prefix.
To do this, shift both to the right till they are equal.
Once they are equal, then shift it back to the number of times it was shifted to add zeros to the right end.
This is the solution.
Examples:
left = 9, right = 12
9 = 1001, right = 1100
Shift once; left = 100, right = 110.
Shift twice; left = 10, right = 11.
Shift thrice; left = 1, right = 1. They are equal, now shift back 3 times.
We get 1000, this is 8, that is the answer.

left = 6, right = 7.
6 = 110, 7 = 111.
Shift once; left = 11, right = 11. They are equal, now shift back 1 time.
We get 110, this is 6, that is the answer.

O(1) time since the loop goes to at max 32.
O(1) space.
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        times_shifted = 0
        while left < right:
            times_shifted += 1
            left = left >> 1
            right = right >> 1
        
        # shift it back, this will add zeros
        return left << times_shifted
