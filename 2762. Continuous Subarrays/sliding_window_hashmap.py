"""
Sliding window with frequency hashmap.
Maintain hashmap of all numbers and their freq in current window.
If freq of any num falls to 0, remove it from the hashmap.
Move left pointer if max(freq) - min(freq) > 2.

O(n^2) time for sliding window and within that min and max calls to the hashmap.
O(n) space used by the hashmap.
"""

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        freq = {}
        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] not in freq:
                freq[nums[r]] = 0
            freq[nums[r]] += 1

            while freq and (max(freq) - min(freq) > 2):
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            
            res += (r-l+1)
        
        return res
