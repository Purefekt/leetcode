"""
Sliding window
Get the first sliding window, which begins at 0th index and has length k.
Count the number of vowels in this and set it to max count.
Now loop from k till n, where n is the length of s.
Each time we move the window by 1 position to the right, so we discard the element at i-k and add the ith element.
So we update the current count accordingly and update max_count.

O(n) time since we go through the string s once.
O(1) space to store the vowels set, current and max count vars
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set(['a', 'e', 'i', 'o', 'u'])

        # get the initial length
        cur_count = 0
        for i in range(k):
            if s[i] in vowels:
                cur_count += 1
        
        max_count = cur_count

        for i in range(k, len(s)):
            # dec cur_count if s[i-k] in vowels, and inc cur_count if s[i] in vowels
            if s[i-k] in vowels:
                cur_count -= 1
            if s[i] in vowels:
                cur_count += 1
            
            max_count = max(max_count, cur_count)
        
        return max_count
