class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # get the next largest number for all in nums2
        next_largest = [-1] * len(nums2)
        stack = []
        for i,n in enumerate(nums2):
            while stack and stack[-1][0] < n:
                _, prev_idx = stack.pop()
                next_largest[prev_idx] = n
            stack.append((n,i))
        
        # get the index of each num in nums2
        indexes = {}
        for i,n in enumerate(nums2):
            indexes[n] = i
        
        # build result
        res = []
        for n in nums1:
            idx = indexes[n]
            res.append(next_largest[idx])
        
        return res
        