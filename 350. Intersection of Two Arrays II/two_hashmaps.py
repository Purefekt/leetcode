"""
use two hashmaps. key -> num : val -> count. Take the smaller list, iterate over the nums and see if it appears in the hashmap of the larger list. Use the min count of both and add to a intersection list. Remove the element from hashmap of the larger list to avoid repetitions.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        freq_1 = collections.Counter(nums1)
        freq_2 = collections.Counter(nums2)

        res = []
        for k,v in freq_1.items():
            if k in freq_2:
                for i in range(min(v, freq_2[k])):
                    res.append(k)
        
        return res
