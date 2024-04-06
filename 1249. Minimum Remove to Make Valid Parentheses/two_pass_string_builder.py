"""
Two pass string builder.
In one pass go from left to right and remove all closing brackers '(' which are extra.
Do this by keeping a track of the net total of brackets. If we see open bracket, increment, if we see closing then decrement.
If we see a closing bracket and net sum is 0, this means this is invalid and dont add it to the string.
Then do this in reverse, go from right to left for the string of the output of the first pass.
This time do it for opening brackets.
Return reverse of the output string of the second pass.

O(n) time for 2 passes over string s.
O(n) space used for creating string of the output of first pass.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # in one pass, do not include closing bracket if we go in negative net
        cur = 0
        res = ""
        for c in s:
            if c != '(' and c != ')':
                res += c
            else:
                if c == '(':
                    res += c
                    cur += 1
                else:
                    if cur > 0:
                        res += c
                        cur -= 1
                    else:
                        continue
        
        # in another pass, do not include opening bracket if we go in negative net. This pass over res
        s = ""
        cur = 0
        for i in range(len(res)-1, -1, -1):
            if res[i] != '(' and res[i] != ')':
                s += res[i]
            else:
                if res[i] == ')':
                    s += res[i]
                    cur += 1
                else:
                    if cur > 0:
                        s += res[i]
                        cur -= 1
                    else:
                        continue
        
        return s[::-1]
        