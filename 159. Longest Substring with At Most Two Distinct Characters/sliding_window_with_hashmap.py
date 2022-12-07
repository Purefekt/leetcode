"""
Sliding window with hashmap
maintan a hashmap of character:last_position
keep 2 pointers l and r for the sliding window
Keep adding characaters to the hashmap and updating its last position
When our hashmap has 3 keys, it means we have 3 distinct chars. We must remove the char with the least last position
Get min value key and set left to min val + 1 and delete this key-value pair
Keep updating max_len

O(n) time. One pass over all characters
O(1) space to store a hashmap of at most 3 keys 
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        hashmap = {}
        max_len = 0
        l = 0
        r = 0

        while r<len(s):
            hashmap[s[r]] = r
            if len(hashmap) > 2:
                min_key = min(hashmap, key=hashmap.get)
                min_val = hashmap[min_key]
                l = min_val+1
                del hashmap[min_key]
            r += 1
            max_len = max(max_len, r-l)
        
        return max_len
