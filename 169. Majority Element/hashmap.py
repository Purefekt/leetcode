"""
Build a counter hashmap and return the key with max value
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = collections.Counter(nums)
        majority_val = len(nums) // 2 + 1
        
        for k,v in counter.items():
            if v >= majority_val:
                return k
            