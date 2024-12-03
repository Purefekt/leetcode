"""
Just create the result by using the indexes given.

O(n) time to go over spaces where n is the size of spaces.
O(s) space to store in res list.
"""

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        cur = 0
        res = []
        for size in spaces:
            res.append(s[cur:size])
            cur = size
        res.append(s[cur:])
        
        return ' '.join(res)
