"""
Since k can be 10^9, we can reduce it to size of n which is at max 10^5.
First k %= sum(chalk).
Now we have just enough k to go for 1 final iteration.
Iterate till k>0 and remove chalk[i] amount each time.
When k goes below 0, this index is our solution.

O(n) time where n is the size of chalk array.
O(1) space
"""

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        total = sum(chalk)
        k %= total

        res = 0
        while k>0:
            if k < chalk[res]:
                return res
            k -= chalk[res]
            res += 1
        
        return res
        