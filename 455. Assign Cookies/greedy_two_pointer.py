"""
Greedy and two pointer.
Sort both lists.
Keep a pointer at the start of both lists.
Move both pointers is g<=s, else just move s pointer.

O(nlogn + mlogm) time where n is length of g and m is length of s.
O(m+n) space for sorting both lists
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()

        g_pointer = 0
        s_pointer = 0

        res = 0
        while g_pointer < len(g) and s_pointer < len(s):
            if g[g_pointer] <= s[s_pointer]:
                res += 1
                g_pointer += 1
                s_pointer += 1
            
            else:
                s_pointer += 1
        
        return res
        