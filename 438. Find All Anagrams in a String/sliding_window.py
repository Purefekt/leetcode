"""
Sliding window over s
We create a 26 length vector for the count of all letters in p
Use a sliding window of size len(p) over s and check the count vector for that window, if same as p vector then append its start to res

O(n) time where n is the size of s
O(1) space since the array will always be of size 26
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        res = []

        if len(p) > len(s):
            return res
        
        # form vector for p
        p_vector = [0 for i in range(26)]
        for c in p:
            p_vector[ord(c) - ord('a')] += 1
        
        # sliding window over s
        # get the initial vector
        window_vector = [0 for i in range(26)]
        for c in s[:len(p)]:
            window_vector[ord(c) - ord('a')] += 1
        
        l = 0
        r = len(p)-1
        while r<len(s):
            if p_vector == window_vector:
                res.append(l)
            
            # update window vector, l and r
            window_vector[ord(s[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r<len(s):
                window_vector[ord(s[r]) - ord('a')] += 1
        
        return res
        