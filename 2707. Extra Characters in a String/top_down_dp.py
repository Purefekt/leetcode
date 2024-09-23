"""
Top down do similar to word break but we can legally break at any char.
Only difference is that if a word exists in the dict, it will result in 0 being added.
And if the word doesnt exist in dict, we add len(word) in that path.
Memoiz over the index where we break.

O(n^3) time since we run the helper function n times, for each call we run a loop of size n and we create a new substring within that which takes n time as well.
O(n + m*k) space since the stack takes n space and the hashset takes m*k space where m is average length of strings in dictionary and k is the length of the dictionary.
"""

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dictionary = set(dictionary)

        memo = {}
        def helper(start):
            if start in memo:
                return memo[start]
            if start  == len(s):
                return 0
            
            res = math.inf
            for i in range(start, len(s)):
                # break at i
                break_string = s[start:i+1]
                extra_chars = len(break_string) if break_string not in dictionary else 0
                res = min(
                    res, extra_chars + helper(i+1)
                )
            memo[start] = res
            return res
        
        return helper(0)
