"""
Greedy
First check if it is possible.
If sum of remaining n/n > 6 or sum of remaining n < n (cannot even assign 1 to all n) or if is it not divisble as integer, it is not possible.
Create res array of size n of all 0s.
Keep incrementing each position by 1 and repeat.

O(m+n) time since getting sum of rolls takes m time and then we iterate through sum(n) where each index can be at max update 6 times, so we go down to 6*n.
O(1) space.
"""

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        # get sum of n
        total_rolls = len(rolls) + n
        total_sum = total_rolls * mean
        total_n = total_sum - sum(rolls)

        if total_n/n > 6 or total_n < n or (total_n//n) != total_n//n:
            return []
        
        res = [0] * n
        idx = 0
        for _ in range(total_n):
            res[idx] += 1
            idx += 1
            idx %= n
        
        return res
