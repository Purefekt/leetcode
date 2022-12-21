"""
Kind of like House Robber [DYNAMIC PROGRAMMING]
Get the frequencies of all numbers and store in a hashmap. Key=number : value=number*frequency
Get a list of all keys in the previous hashmap (only unique nums) and sort it
initialize a dp array of len(unique nums)
dp[0] means when we only have the nums[0] number to choose from, get its value from freq hashmap
dp[1] will either be freq[nums[1]]+dp[0] if nums[0] and nums[1] are NOT consecutive, else it will be max(freq[nums[1]], dp[0])
Fill the dp array from 2nd element till end and keep updating in a similar manner as dp[1]

O(nlogn) time. n to build freq hashmap, nlogn to sort keys, n to fill dp
O(n) space to store in dp array
"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = n
            else:
                freq[n] = freq[n] + n
        
        # get keys and sort
        nums = list(freq.keys())
        nums.sort()

        # if only 1 unique number, return number*freq
        if len(nums)<2:
            return freq[nums[0]]

        dp = [0 for i in range(len(nums))]
        dp[0] = freq[nums[0]]
        if nums[1] == nums[0]+1:
            dp[1] = max(freq[nums[1]], dp[0])
        else:
            dp[1] = dp[0] + freq[nums[1]]
        
        for i in range(2,len(dp)):
            if nums[i-1] == nums[i]-1:
                dp[i] = max(freq[nums[i]] + dp[i-2], dp[i-1])
            else:
                dp[i] = freq[nums[i]] + dp[i-1]
        
        return dp[-1]
