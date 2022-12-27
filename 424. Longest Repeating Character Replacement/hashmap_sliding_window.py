"""
Create a hashmap to store the frequencies of each letter in a given substring
The freq will be updated using a sliding window. Initialize the hashmap for all uppercase english letters with val 0
Start the sliding window with l and r at 0 and maintain a result variable to track the longest valid substring
for a given substring, get the frequency value of the most frequent character. For 'AABA', we will have A:3, B:1 and the most freq value will be 3
Suppose k is 2, which, for this current substring we will see the min number of subs, which is length - most freq val, 4-3 = 1. Since 1 is <= k which means we can make the substitutions and have a valid substring of length 4.
Move the right pointer till we get valid substrings, if we get an invalid one, move the left pointer and update the hashmap (by decreasing the freq of the letter removed)

O(26*n) time
O(1) space 
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}
        for i in range(26):
            freq[chr(ord('A') + i)] = 0
        
        # sliding window
        l = 0
        r = 0
        res = 0
        while r<len(s):
            freq[s[r]] += 1
            most_freq = max(freq.values())
            curr_ss_len = r-l+1
            
            if curr_ss_len - most_freq <= k:
                res = max(res, curr_ss_len)
                r += 1
            
            else:
                freq[s[l]] -= 1
                l += 1
                r += 1
        
        return res
