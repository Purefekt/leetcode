"""
Greedy
We basically need to find the number of 0s which lie in front of a 1.
For 1000, we need 3 swaps for it since we need to swap with each 0.

O(n) time.
O(1) space.
"""

class Solution:
    def minimumSteps(self, s: str) -> int:
        
        # get the number of 0s ahead of each position
        num_zero = 0
        res = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                num_zero += 1
            else:
                res += num_zero
        
        return res