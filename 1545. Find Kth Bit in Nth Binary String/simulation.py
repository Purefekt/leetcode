"""
Simulate the string building process.

O(2^n) time since the size of string can become 2^n-1 and we need to build all of them.
O(2^n) space.
"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        if n == 0:
            return "0"
        
        # build the string
        prev = "0"
        cur = ""
        for i in range(n):
            prefix = prev
            middle = "1"
            suffix = [c for c in prev[::-1]]
            for j in range(len(suffix)):
                suffix[j] = "1" if suffix[j] == "0" else "0"
            suffix = ''.join(suffix)
            cur = prefix + middle + suffix
            prev = cur
        
        return cur[k-1]
