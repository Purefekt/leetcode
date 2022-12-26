"""
Dynamic Programming O(n^2)
For each index, we either keep it in the subsequence or not
Create a dp array of len(nums). We fill it from the right side
The last element will be value 1, this is when we have an array of nums with just the last element, thus the LIS will be of length 1
Start filling right to left, for each index, the max substring will be either 1 or 1+dp[idx] IF that index element is larger than current idx element
for array [1,2,3], dp initially = [0,0,1]. Then we find dp[1] which is max(1, dp[2]), then we find dp[0] which is max(1, dp[1], dp[2])
Return the max of dp array.

O(n^2) time. O(n) for every idex and a nested O(n) scan to find the max val
O(n) space to store dp array
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [0 for i in range(len(nums))]
        dp[-1] = 1

        for i in range(len(nums)-2, -1, -1):
            maxx = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    cur_max = 1+dp[j]
                    maxx = max(maxx, cur_max)
            dp[i] = maxx
        

        return max(dp)
