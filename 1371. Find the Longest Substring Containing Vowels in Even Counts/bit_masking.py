"""
Bitmasking.
We dont care about which vowel has how many numbers, but just that if all are even or not.
We also dont care about any consonants.
We can set the state of weather a vowel is even as 0 or odd as 1.
Since we have 5 vowels, we can use 5 bits, 00000 means all are even.
We can have 32 different possibilities for this bit mask, 2^5.
Represent all consonants as 0 and each vowel as increasing power of 2.
a = 1, b = 0, c = 0, d = 0,...e = 2, ...,i = 4,...,o = 8,...,u = 16,...z = 0.
Initialize mp array of size 32 with all -1. This will store the first occurance of a value of prefix xor.
Get the prefix xor of s using the char mask.
If p_xor hasnt been seen before aka it mp[p_xor] == -1 and p_xor is not 0, update its index to i.
Update result to the diff between current index and mp[p_xor]. If we just added it, then it will simply be 0.

O(n) time.
O(1) space.
"""

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        p_xor = 0
        # consonants get 0, vowels get powers of 2
        chars = [0] * 26
        chars[ord('a') - ord('a')] = 1
        chars[ord('e') - ord('a')] = 2
        chars[ord('i') - ord('a')] = 4
        chars[ord('o') - ord('a')] = 8
        chars[ord('u') - ord('a')] = 16

        mp = [-1] * 32
        res = 0

        for i in range(len(s)):
            p_xor ^= chars[ord(s[i]) - ord('a')]
            # if p_xor is not 0 and it hasnt been seen before, set its index
            if mp[p_xor] == -1 and p_xor != 0:
                mp[p_xor] = i
            
            res = max(res, i-mp[p_xor])
        
        return res
