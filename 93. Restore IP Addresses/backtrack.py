"""
Backtrack and place dots and see if it is valid
If the input string has more than 12 chars, this can never be a valid ip address
The recursive function will take the index after which we want to put a dot, number of dots already used and the current string formed
For each index, we can place the dot either after s[index:index+1], s[index:index+2], s[index:index+3], thus we run a for loop 3 times for this.
NOTE: it can be that we might go beyond the length of s when trying to add the dot, thats why we will go till min(index+3, len(s)) to remain in bounds
Also check for the validity of the integer chunk, it must be <256 and numbers like 002 or 022 are invalid due to leading zeros. Handle this with checking the length of the string version and integer version.

O(m^n) time or O(1) since here m=3 and n=4. The height of the decision tree will be at max 4 and each time we have 3 decisions. 
O(m*n) for stack size
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) > 12:
            return

        res = []
        def backtrack(idx, dots, cur_ip):
            # if we have placed 4 dots and index is at the end
            if dots == 4 and idx == len(s):
                res.append(cur_ip[:-1])
                return
            
            # if we exceed 4 dots but have not reached the end of the string, its invalid
            if dots > 4:
                return


            for j in range(idx, min(idx+3, len(s))):
                # check if its a valid number
                cur_integer = int(s[idx:j+1])
                if cur_integer < 256 and len(s[idx:j+1]) == len(str(cur_integer)):
                    backtrack(j+1, dots+1, cur_ip + s[idx:j+1] + '.')
        
        backtrack(0,0,'')
        return res
