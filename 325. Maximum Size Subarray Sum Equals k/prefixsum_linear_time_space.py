"""
O(N) time and space. Solve with prefixsum

get the prefixsum for all arrays from 0 to i. On each iteration check if prefixsum-k appears in the indicies dict.
indicies dict = {prefixsum:index}
If it appears then update longestsubarray to max(longestsubarray, i - indicies[prefixsum-k])
add the current prefix sum and its index to the indicies hashmap only if it doesnt exist. 
NOTE: if we need to find the shortest subarray, then we update the hashmap everytime and use min.
"""

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        prefixsum = 0
        indicies = {}
        longestsubarray = 0
        
        for i in range(len(nums)):
            prefixsum += nums[i]
            
            # if the prefixsum till i ==k, then it is by default the longestsubarray till length i
            if prefixsum == k:
                longestsubarray = i+1
            
            if prefixsum-k in indicies.keys():
                longestsubarray = max(longestsubarray, i-indicies[prefixsum-k])
                
            if prefixsum not in indicies.keys():
                indicies[prefixsum] = i
        
        return longestsubarray
    