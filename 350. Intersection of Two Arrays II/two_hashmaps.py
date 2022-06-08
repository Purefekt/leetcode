"""
use two hashmaps. key -> num : val -> count. Take the smaller list, iterate over the nums and see if it appears in the hashmap of the larger list. Use the min count of both and add to a intersection list. Remove the element from hashmap of the larger list to avoid repetitions.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap1 = {}
        hashmap2 = {}
        
        # populate the hashmaps with count of each num
        for n in nums1:
            if n not in hashmap1.keys():
                hashmap1[n] = 1
            else:
                hashmap1[n] += 1
        
        for n in nums2:
            if n not in hashmap2.keys():
                hashmap2[n] = 1
            else:
                hashmap2[n] += 1
        
        # use the smaller list and iterate over its elements. Compare with the larger list's hashmap
        intersection = []
        # if list1 is smaller
        if len(nums1) < len(nums2):
            for n in nums1:
                if n in hashmap2.keys():
                    # intersection will be the min of count in both hashmaps
                    num_common_count = min(hashmap1[n], hashmap2[n])
                    # add this number num_common_count amounts of times
                    for i in range(0, num_common_count):
                        intersection.append(n)
                
                    # remove this element from the hashmap
                    hashmap2.pop(n)
        
        else:
            for n in nums2:
                if n in hashmap1.keys():
                    num_common_count = min(hashmap1[n], hashmap2[n])
                    for i in range(0, num_common_count):
                        intersection.append(n)
                
                    hashmap1.pop(n)
        
        return intersection
    