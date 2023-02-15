"""
Recursion with memoization
we start with index 0, see the substring s[0:1] and verify if its in the wordDict
If it is not then we try s[0:2] and all the way till s[0:len(s)]
If a substring is in the worddict we check form substrings starting from where the previous substring ended
Base case if when we read index = len(s), return True

O(n^3) time since the length of s is n and for each we can check upto n times. Also substring computation is linear time thus another n
O(n) space for the stack and memoization table
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)

        memo = {len(s):True}

        def backtrack(idx):
            if idx in memo:
                return memo[idx]
            
            for i in range(idx+1, len(s)+1):
                if s[idx:i] in wordDict:
                    if backtrack(i) is True:
                        memo[idx] = True
                        return True
            
            memo[idx] = False 
            return False

        return backtrack(0)
