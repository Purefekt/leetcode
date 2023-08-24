"""
Get the amount required by the remaining n rolls.
If this is less than n or larger than 6*n, we cannot construct this using a 6 sided die.
Create a result array of 0s and keep adding 1 to each and repeat till we reach remaining amount.

O(n) time to iterate over remaining sum.
O(1) space to track constants like rolls_sum, total_sum and rem_sum. res is a part of output and wont be used for space complexity.
"""

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        m = len(rolls)

        rolls_sum = sum(rolls)
        total_sum = (m+n) * mean
        rem_sum = total_sum - rolls_sum

        if rem_sum < n or rem_sum > 6*n:
            return []
        
        # distribute the remaining sum over equally
        res = [0] * n
        for i in range(rem_sum):
            idx = i%n
            res[idx] += 1
        
        return res
