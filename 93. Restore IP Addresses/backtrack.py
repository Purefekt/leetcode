"""
If len(s) is greater than 12, we can never make a valid ip address, return []
Backtracking. The recursive func will take current combo, number of dots and index.
If the number of dots == 4 and the index == len(s), this means we have placed all dots and used all chars, this is a valid ip.
We need to add either 1 char, 2 chars or 3 chars to the combination. Adding 1 char is done without any conditions
To add 2 chars, we first check if index+1 exists in the length, if yes then we check if the first char must not be a '0', since '01' is invalid.
To add 3 chars, we check if index+2 is in the length, if yes then we check if the first char must not be '0' and first 2 chars must not be '00' and the number must not be larger than 255.

O(m^n) time or O(1) since here m=3 and n=4. The height of the decision tree will be at max 4 and each time we have 3 decisions. 
O(m*n) for stack size
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) > 12:
            return []
        
        res = []
        def backtrack(combo, dots, idx):
            if dots == 4 and idx == len(s):
                res.append('.'.join(combo.copy()))
                return
            
            if idx == len(s):
                return
            
            # add 1 char
            combo.append(s[idx:idx+1])
            backtrack(combo, dots+1, idx+1)
            combo.pop()

            # add 2 chars
            if idx < len(s)-1 and s[idx] != '0':
                combo.append(s[idx:idx+2])
                backtrack(combo, dots+1, idx+2)
                combo.pop()
            
            # add 3 chars
            if idx < len(s)-2 and s[idx] != '0' and s[idx:idx+2] != '00' and int(s[idx:idx+3]) < 256:
                combo.append(s[idx:idx+3])
                backtrack(combo, dots+1, idx+3)
                combo.pop()
        
        backtrack([],0,0)
        return res
