"""
Recursion with memoization.
We basically have to create the longest increasing subsequence.
We have 2 arrays, we create 2 pointers, i for nums1 and j for nums2.
Base case, if either of i or j exceed the lengths of nums1 or nums2 respectively, then return 0.
If nums1[i] == nums1[j], then we can increment both counters while adding 1 to the solution since a direct connection is the most optimal.
Else we will first set nums1 element and move j pointer and then we will set nums2 element and move i pointer and take the max.

O(n1*n2) time.
O(n1*n2) space for the memoization table
"""

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo = {}

        def helper(i,j):

            if i == len(nums1) or j == len(nums2):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            # if equal, create a connection and increment both pointers
            if nums1[i] == nums2[j]:
                memo[(i,j)] = 1 + helper(i+1, j+1)
            else:
                # keep nums1 pointer same and try to find a match for it by moving nums2 pointer
                n1 = helper(i, j+1)
                # keep nums2 pointer same and try to find a match for it by moving nums1 pointer
                n2 = helper(i+1, j)

                memo[(i,j)] = max(n1, n2)
            
            return memo[(i,j)]
        
        return helper(0,0)
