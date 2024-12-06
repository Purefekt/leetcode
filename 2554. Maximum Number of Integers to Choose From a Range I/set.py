"""
Hashset to track banned.
Go from 1 to n and get max number of nums we can keep till maxSum.

O(n+m) time. m time to create banned set and n to create res.
O(m) space where m is size of banned set.
"""

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        banned = set(banned)
        total = 0
        res = 0

        for i in range(1, n+1):
            if i in banned:
                continue
            if total + i <= maxSum:
                res += 1
                total += i
            else:
                return res
        
        return res
