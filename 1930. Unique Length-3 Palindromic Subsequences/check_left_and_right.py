"""
Since the palindrome should be of length 3, the middle character doesnt matter and only the left side and right side characters must be same.
Since the input contains only lowercase english letters, when we set any element to the middle (except first and last element), then there can be 26 different palindromes for each letter.
Suppose we have aba, then we set b as the middle and then we need to find if there exists a on either side of b, then we need to check if b exists on either side of b and so on till z. 
Create a hashmap of the first occurance of each element in s, do the same for last occurance of each element.
Loop from 1 -> len(s)-1, set each index to  mid and then run a loop from 'a' -> 'z' and check if the first occurance is less than mid index and the last occurance is larger than mid index.
Add this to a set to keep uniques and return length of this set.

O(26*n) time. Outer loop of size n-2 and inner loop of size 26.
O(n) space to store the hashmaps and result set
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        earliest = {}
        latest = {}

        for i,c in enumerate(s):
            if c not in earliest:
                earliest[c] = i
            latest[c] = i
        
        res = set()
        for i in range(1, len(s)-1):
            for j in range(ord('a'), ord('z')+1):
                c = chr(j)

                if c in earliest and c in latest and earliest[c] < i < latest[c]:
                    palindrome = c + s[i] + c
                    res.add(palindrome)
        
        return len(res)
