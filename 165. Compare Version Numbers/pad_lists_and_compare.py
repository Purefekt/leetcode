"""
Split both versions using '.' and get lists of tokens
Run a for loop for the max len of either versions
Add a condition to append a 0 for the smaller version
compare each and return based on condition

O(n + m + max(n,m)). O(n) to build the list for version1, O(m) to build the list of version2 and O(max(m,n)) to iterate over both lists
O(n+m) space to store both lists
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        # get lists for both versions
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        for i in range(max(len(v1), len(v2))):
            if i>=len(v1): v1.append('0')
            if i>=len(v2): v2.append('0')
            
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                continue
        
        return 0
        