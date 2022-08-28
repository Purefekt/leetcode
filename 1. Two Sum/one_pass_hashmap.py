"""
As we add to the hashmap, check if a pair exists and return.
Instead of building the entire map
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # pairs = target-nums[i]:i
        pairs = {}
        
        for i in range(len(nums)):
            if nums[i] in pairs:
                return [i, pairs[nums[i]]]
            pairs[target - nums[i]] = i
            