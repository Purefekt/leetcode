"""
Backtrack. Recursively
At each level, append the current combination to the result

O(n * 2^n) to get all combinations and copy them
O(n) space to maintain current combo
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(start, combo):

            res.append(combo.copy())

            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(i+1, combo)
                combo.pop()
        
        backtrack(0, [])
        return res
