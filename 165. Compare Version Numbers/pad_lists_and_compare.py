"""
Split the tokens and get lists of all versions
Run a for loop for the range of the larger list. On every token compare their int values and return if one is larger than the other
To check for if the smaller list is out of range, then substitute that value as 0
if the for loop terminates without return, both are equal

O(max(m,n)) time where m is version1 len and n is version2 len
O(n+m) space since we need to store these two lists
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        # split the tokens
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        # go over the len of the larger and compare
        for i in range(max(len(v1), len(v2))):
            
            # these statements to check for out of range error
            if i >= len(v1):
                n1 = 0
            else:
                n1 = int(v1[i])
            
            if i >= len(v2):
                n2 = 0
            else:
                n2 = int(v2[i])
            
            # compare
            if n1 > n2:
                return 1
            elif n2 > n1:
                return -1
        
        return 0
    