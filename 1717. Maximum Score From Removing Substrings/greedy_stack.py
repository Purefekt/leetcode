"""
Greedy, stack, two pass.
It is always optimal to remove the substring with the higher points, call this good and call the other bad.
First remove all the good substrings. Use a stack to do it efficiently.
Then another pass to remove all bad substrings.
While doing this, track the removals to add points.

O(n) time for 2 linear passes over the input.
O(n) space used by stack.
"""

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        good, bad = 'ab', 'ba'
        points = {
            good: x,
            bad: y
        }
        if y>x:
            good, bad = bad, good
        
        res = 0
        # first pass to remove better substring
        stack = []
        for c in s:
            if stack and stack[-1] + c == good:
                stack.pop()
                res += points[good]
            else:
                stack.append(c)
        
        s = ''.join(stack)
        # second pass to remove worse substring
        stack = []
        for c in s:
            if stack and stack[-1] + c == bad:
                stack.pop()
                res += points[bad]
            else:
                stack.append(c)
        
        return res
