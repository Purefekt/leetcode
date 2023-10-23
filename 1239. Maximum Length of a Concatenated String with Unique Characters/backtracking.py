"""
Backtracking.
Try every single combination of words in an ordered manner and check if the current concatonated word is valid.
Check this easily by checking len(word) == len(set(word)). If this is false, then return 0.
result will be len(set(word)), then run a loop from the current word's position till end of array.
Update res to be max of res and the recursion solution.

O(2^n) time where n is the length of array. Since we are exploring the entire tree.
O(n) space for stack
"""

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def helper(start, word):
            if len(word) != len(set(word)):
                return 0
            
            res = len(set(word))
            
            for i in range(start, len(arr)):
                res = max(res, helper(i, word + arr[i]))
            
            return res
        
        return helper(0, "")
        