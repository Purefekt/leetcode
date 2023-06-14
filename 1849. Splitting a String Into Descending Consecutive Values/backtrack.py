"""
Backtrack
Try every split, if we get a valid combination, then return True.
backtrack func will take the current combo and the current start index, everything before this index has been split.
Loop from start index till the end and try all splits of size 1,2,3,...
Get the next_num as an integer to get rid of leading zeros, if current combo is empty ie it is the first number added, simply add.
If there already exists numbers in the combo, then ONLY add if the next_num is the next smaller consecutive number.

O(n^n) time. But it will be more efficient since we perform the pruning step.
O(n) space for recursion stack
"""

class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(combo, start):
            if start == len(s) and len(combo)>1:
                return True
            
            for i in range(start+1, len(s)+1):
                next_num = int(s[start:i])

                if not combo:
                    combo.append(next_num)
                    if backtrack(combo, i) is True:
                        return True
                    combo.pop()
                
                else:
                    if next_num == combo[-1] - 1:
                        combo.append(next_num)
                        if backtrack(combo, i) is True:
                            return True
                        combo.pop()
            
            return False
        
        return backtrack([], 0)
        