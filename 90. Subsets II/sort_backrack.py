"""
Sort the nums, this will help in avoiding duplicates
Use backtracking and add the current combo in every level of the tree
Recursive function takes the current combo and index we are at
Base case if index == len(nums), return
Iterate through all remaining nums in the array starting at idx, to avoid duplicates, maintain a prev var and skip if nums[i] == prev

O(n*2^n) time. 2^n time to build the decision tree and n time to create a deep copy of the combination every time to add it to res
O(n) space. Sorting takes O(n) time and the stack takes O(n) space
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def backtrack(combo, idx):
            res.append(combo.copy())

            if idx == len(nums):
                return
            
            prev = None
            for i in range(idx, len(nums)):
                if nums[i] != prev:
                    combo.append(nums[i])
                    backtrack(combo, i+1)
                    combo.pop()

                    prev = nums[i]

        backtrack([], 0)
        return res
        