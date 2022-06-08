class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # convert array to set
        set1 = set(nums1)
        set2 = set(nums2)
        
        # use the smaller set to iterate over the larger set (further optimize)
        intersection = []
        # if set1 is smaller
        if len(set1) < len(set2):
            for n in set1:
                if n in set2:
                    intersection.append(n)
        # if set2 is smaller or both are equal
        else:
            for n in set2:
                if n in set1:
                    intersection.append(n)
        
        return intersection
    