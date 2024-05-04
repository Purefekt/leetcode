class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        
        difference = []
        for i in range(len(nums1)):
            difference.append(nums1[i] - nums2[i])
        
        difference.sort()

        l = 0
        r = len(difference)-1

        res = 0
        while l<r:
            if difference[r] + difference[l] > 0:
                res += r-l
                r -= 1
            else:
                l += 1
        
        return res
        