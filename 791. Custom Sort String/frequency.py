"""
Create hashmap of frequency of each char in s.
Iterate through chars in order and if they exist in freq, add that char * value number of times to res.
Then remove this key value pair from freq.
Now iterate through the hashmap and add the char * value to res, these are all remaining chars.

O(n) time where n is the size of s.
O(n) space.
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1
        
        res = ""
        for c in order:
            if c in freq:
                res += c*freq[c]
                del freq[c]
        
        for k,v in freq.items():
            res += k*v
        
        return res
