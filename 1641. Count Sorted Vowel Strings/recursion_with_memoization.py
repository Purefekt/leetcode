"""
Top down DP. Recurison with memoization
For each level, we add a vowel to the string, base case is if the length of the string == n
We do not need the string and just its length. We will also use the vowels array which is sorted which will let us build the string in lexicographical order
Use a memoization table to store the pairs (string_len, vowel_idx)

O(n*5) time. which is O(n) time. we check till the length is n and the vowel index is 5. We check once for each since we are using memoization
O(n*5) space to store the memoization table and stack size
"""

class Solution:
    def countVowelStrings(self, n: int) -> int:

        vowels = ["a","e","i","o","u"]

        memo = {}
        
        def backtrack(string_len, vowel_idx):

            if string_len == n:
                return 1
            
            res = 0
            for i in range(vowel_idx, 5):
                res += backtrack(string_len+1, i)
            
            memo[(string_len, vowel_idx)] = res
            return res
        
        backtrack(0,0)
        return memo[(0,0)]
