"""
Create 2 counter lists of size 26 for all alphabets
populate them using index0 = a, index25 = z
compare and get absolute diff
result will be half of the diff
"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count_1 = [0]*26
        count_2 = [0]*26
        
        for c in s:
            count_1[ord(c)-ord('a')] += 1
        for c in t:
            count_2[ord(c)-ord('a')] += 1
        
        # get abs difference
        result = 0
        for i in range(26):
            result += abs(count_1[i] - count_2[i])
        
        return result//2
    