"""
DP solution. 2D dp for 2 arrays.
Create a DP matrix of size n1+1 * n2+1, where n1 = len(nums1) and n2 = len(nums2).
Fill this with zeros.
The first row means that we have a complete array nums2 and an empty array nums1. The reverse for cols.
DP rule, if nums1[i-1] == nums2[j-1], then add 1 + diagnally left
Else, max of left and top.

O(n1*n2) time.
O(n1*n2) space. Can be optimized to use a single array.
"""

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = []
        for i in range(len(nums1)+1):
            dp_row = []
            for j in range(len(nums2)+1):
                dp_row.append(0)
            dp.append(dp_row)
        
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                # if same, then take diagnally left + 1
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                # if different, then take max(left, top)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
