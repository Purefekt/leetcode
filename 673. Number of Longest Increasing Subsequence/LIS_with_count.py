"""
Similar to LIS problem
LIS[-1] will always be one. We need to also maintain the count of sequences at that index thus NumberOfLIS[-1] = 1
Dp array will be a 2D matrix of size 2*n. First row is for LIS and second row is for NumberOfLIS
Start from the 2nd last element, fill right to left
Find the max length of subsequence starting from that index same as LIS problem. Default case is 1. If maxval remains 1, this means no subsequence found, the LIS will be 1 and number of seq will be 1
If the max val > 1, do another pass and check all the indexes where this was true, sum their number of sequences to be the number of sequences of this index
After filling the dp matrix, get the longest subsequence legnth, for all the indexes with this length sum up the number of sequences. This is the total number of sequences 

O(n^2) time. to fill the dp matrix
O(n) space to store dp matrix
"""

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        dp = [0 for i in range(len(nums))]
        dp[-1] = [1,1]

        for i in range(len(dp)-2, -1, -1):
            # get the max possible val
            max_val = 1
            for j in range(i+1, len(dp)):
                if nums[i] < nums[j]:
                    max_val = max(max_val, 1 + dp[j][0])

            num_sequences = 0
            if max_val == 1:
                dp[i] = [1,1]
            else:
                for j in range(i+1, len(dp)):
                    if nums[i] < nums[j]:
                        if 1 + dp[j][0] == max_val:
                            num_sequences += dp[j][1]
                dp[i] = [max_val, num_sequences]
        
        # get the max len
        max_len_ss = max(dp)[0]

        max_sequences = 0
        for i in range(len(dp)):
            if dp[i][0] == max_len_ss:
                max_sequences += dp[i][1]
        
        return max_sequences
