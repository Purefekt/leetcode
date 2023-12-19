"""
Use sliding window to check if the required chars and their frequencies exists in the current sliding window.
Expand the sliding window towards the right if the condition is not yet satisfied.
If condition is satisfied, shrink from left side till the condition breaks and update the result to smallest window size.
Optimization is required to verify if the window is valid.
Use a hashmap 'need' with the counts of all chars in t. Create a hashmap 'have' with keys same as need and values set to 0.
Use a counter need_count and have_count. need_count is simply the length of t.
have_count will be increased only when it matters. ie suppose we have A:3 in need and A:2 in have and we came accross another A in the window, then we will increase have_count by 1. 
Similarly, if we have A:3 in need and A:3 in have and we encounter another A, we will not increase have_count since it is extra.
We will decrease have_count only when the count of any char dips below the needed. If we have A:3 in need and A:3 in need and we remove an A from the left size, then need_count -= 1.
But if we have A:3 in need and A:4 in have, and we remove an A from the left side, then we dont decrement need_count.
Whenever need_count == have_count, keep shrinking by moving l+=1 and updating the result.

O(s + t) time where s is length of s and t is length of t.
O(t) space to store the hashmaps. 
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        need = {}
        have = {}
        for c in t:
            if c not in need:
                need[c] = 0
                have[c] = 0
            need[c] += 1
        
        need_count = len(t)
        have_count = 0
        
        l = 0
        r = 0
        res = None

        while r<len(s):

            if s[r] in have:
                have[s[r]] += 1
                if have[s[r]] <= need[s[r]]:
                    have_count += 1
            r += 1

            while have_count == need_count:
                if not res:
                    res = [l,r]
                else:
                    if r-l < res[1]-res[0]:
                        res = [l,r]
                
                if s[l] in have:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        have_count -= 1
                l += 1
        
        if not res:
            return ""
        return s[res[0]:res[1]]
            