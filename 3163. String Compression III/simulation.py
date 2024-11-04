"""
Simple simulation with count.
Break when count of current char exceeds 9.

O(n) time.
O(n) space.
"""

class Solution:
    def compressedString(self, word: str) -> str:
        
        char = ''
        count = 0
        res = []
        for c in word:
            if c != char:
                res.append(str(count) + char)
                char = c
                count = 1
            else:
                if count == 9:
                    res.append('9' + char)
                    count = 1
                else:
                    count += 1
        res.append(str(count) + char)
        res = res[1:]
        return ''.join(res)
