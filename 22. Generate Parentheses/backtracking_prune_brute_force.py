"""
Backtracking to prune some branches from the brute force method by passing count of left and right brackets in current combo
If the length of a combo is 2n, we add it to the res. We dont need to check validity since the next 2 statements will gaurantee only valid combos
We can only add n number of left brackets and not more than that
We cant go down a branch where the number of right brackets is already more than left, since this combo will always be invalid

O(k), where k is the number of valid combinations
O(k) for stack depth
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def backtrack(combo,left,right):

            if len(combo) == 2*n:
                if left == right:
                    res.append(''.join(combo))
                return
            
            # can never add more than n left brackets
            if left<n:
                combo.append('(')
                backtrack(combo, left+1, right)
                combo.pop()
            
            # can never add more right brackets than the number of left brackets
            if right<left:
                combo.append(')')
                backtrack(combo, left, right+1)
                combo.pop()
        
        backtrack([], 0, 0)
        return res
