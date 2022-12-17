"""
create 2 lists of frequencies of len 26. list[0] is num of a and list[25] is num of z
for freq of each letter, get abs diff between both. Sum it, this is the total difference in both words
in 1 operation we can replace a non required letter with a required one. This is same as making a difference of 2, thus result will be half of total difference

O(n) time to iterate over both strings of len n. To iterate over the freq lists takes constant time since it is O(26)
O(1) space to store the freq and difference in constant time
"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        # build freq lists
        s_freq = [0 for i in range(26)]
        t_freq = [0 for i in range(26)]

        for i in range(len(s)):
            s_freq[ord(s[i]) - ord('a')] += 1
            t_freq[ord(t[i]) - ord('a')] += 1
        
        # get difference from both freq
        difference = 0
        for i in range(len(s_freq)):
            difference += abs(s_freq[i] - t_freq[i])
        
        return difference//2
        