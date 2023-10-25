"""
Greedy.
Try to include as many characters in a set as possible.
This means only create a new set if a non unique char is found.

O(n) time.
O(1) space. Requires O(26) to store at max 26 unique alphabets.
"""

class Solution:
    def partitionString(self, s: str) -> int:
        
        count = 1
        cur_set = set()

        for c in s:
            if c in cur_set:
                count += 1
                cur_set = set()
                cur_set.add(c)
            else:
                cur_set.add(c)
        
        return count
