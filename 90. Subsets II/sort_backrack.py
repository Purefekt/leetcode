"""
Sort the nums to maintain a deterministic order of the formed tuples
Build the decision tree and add the combination at every level of the tree to the set
Sorting means we will get the same order of tuples for duplicate tuples and using a set will avoid keeping duplicates

O(n*2^n) time. 2^n time to build the decision tree and n time to create a deep copy of the combination every time to add it to res
O(n) space. Sorting takes O(n) time and the stack takes O(n) space
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()

        def backtrack(combo, start):
            res.add(tuple(combo.copy()))

            if len(combo) == len(nums):
                return
            
            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(combo, i+1)
                combo.pop()

        backtrack([], 0)
        return res
        