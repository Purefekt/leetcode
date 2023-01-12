"""
Use a window of size 10 and slide it one by one
Use string slice and add it to a hashmap with its count
Check all the string slices with count >1 and add it to the result

O(n) time
O(n) space
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        if len(s) < 10:
            return []

        count = {}
        
        l = 0
        r = 10
        while r<=len(s):
            seq = s[l:r]
            if seq not in count:
                count[seq] = 1
            else:
                count[seq] += 1
            l += 1
            r += 1
        
        res = []
        for k,v in count.items():
            if v > 1:
                res.append(k)
        
        return res
            