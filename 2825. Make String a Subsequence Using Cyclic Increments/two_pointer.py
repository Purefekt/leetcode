"""
Two pointer.
If pointer at str1 == pointer at str2, simply forward both pointers.
If next char at pointer at str1 == pointer at str2, forward both pointers as well.
In any other case, forward str1 pointer to try the next char.

O(n) time where n is the size of str1.
O(1) space.
"""

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        if len(str1) < len(str2):
            return False
        
        p1 = 0
        p2 = 0

        while p1 < len(str1):
            if str1[p1] == str2[p2]:
                p1 += 1
                p2 += 1
            elif (str1[p1] == 'z' and str2[p2] == 'a') or (chr(ord(str1[p1]) + 1) == str2[p2]):
                p1 += 1
                p2 += 1
            else:
                p1 += 1
            if p2 == len(str2):
                return True
        
        return False
