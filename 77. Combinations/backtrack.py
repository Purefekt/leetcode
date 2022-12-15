"""
Backtrack.

O(k nchoosek) time
O(nchoosek) space
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def backtrack(start, combo):
            if len(combo) == k:
                res.append(combo.copy())
                return
            
            for i in range(start, n+1):
                combo.append(i)
                backtrack(i+1, combo)
                combo.pop()
        
        backtrack(1, [])
        return res
    