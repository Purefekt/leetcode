"""
Create frequency array for s1. Use a sliding window of size len(s1) and create a frequency array for a substring of s2.
For each iteration of sliding window, compare the 2 arrays, if they are equal then a permutation exists.
To create s2_ss_freq, create the first sliding windwo freq and for every subsequent, dec l-1 and increment r. (optimization)
Edge cases, if s2 is smaller than s1 then false. If both string are equal then very first freq array should be the same else false

O(m+n) time. 
O(1) space since the array use constant space of 26
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        # get frequency tuple of s1
        s1_freq = [0 for i in range(26)]
        for c in s1:
            s1_freq[ord(c)-ord('a')] += 1
        
        
        l = 0
        r = len(s1)
        s2_ss_freq = [0 for i in range(26)]
        for c in s2[l:r]:
            s2_ss_freq[ord(c)-ord('a')] += 1
        if s1_freq == s2_ss_freq:
            return True

        if len(s1) == len(s2):
            if s1_freq == s2_ss_freq:
                return True
            return False
        
        # move sliding window of len(s1) over s2. For each iter, check if s1_freq = s2_substring_freq
        l = 1
        r = len(s1) + 1
        while r<=len(s2):
            # dec the l-1 char freq and increment r char freq
            s2_ss_freq[ord(s2[l-1]) - ord('a')] -= 1
            s2_ss_freq[ord(s2[r-1]) - ord('a')] += 1
            if s2_ss_freq == s1_freq:
                return True
            
            l += 1
            r += 1
        
        return False
