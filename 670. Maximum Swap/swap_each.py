"""
Brute force.
Convert to string and try each swap.

O(n^2) time where n is len of num.
O(n) space.
"""

class Solution:
    def maximumSwap(self, num: int) -> int:

        res = num

        if num < 10:
            return num
        
        num = str(num)
        num = [n for n in num]

        for i in range(len(num)):
            for j in range(i+1, len(num)):
                # swap i and j
                new_num = num.copy()
                new_num[i], new_num[j] = new_num[j], new_num[i]
                new_num = int(''.join(new_num))
                res = max(res, new_num)
        
        return res
