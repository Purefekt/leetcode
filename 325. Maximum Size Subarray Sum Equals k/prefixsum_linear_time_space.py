"""
Prefix sum
Build a prefix sum hashmap by iterating nums, one by one. Key=prefix sum : value=index
Initiate the prefix sum map with 0:-1. This means the prefix sum is 0 at index -1. this is to avoid edge cases
Start loop over n, for each iteration update the current prefix sum and add it to the hashmap if that value doesnt exist
Note, if a prefix sum is already in the hashmap, do not add it since we need to maxmimize the substring so we need the left most index
In each iteration check if prefix sum[i] - k is in the hashmap. If it is then we found a valid substring of length i-prefix_sum[cur_psum-k].
This is because for an array of prefix sums, psum[j] - psum[i] = k, we rearrange this

O(n) time
O(n) space
""" 

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        prefix_sum = {0:-1}

        longest_len = 0
        cur_psum = 0

        for i,n in enumerate(nums):
            cur_psum += n
            if cur_psum not in prefix_sum:
                prefix_sum[cur_psum] = i

            if cur_psum - k in prefix_sum:
                cur_ss_len = i-prefix_sum[cur_psum-k]
                longest_len = max(longest_len, cur_ss_len)
        
        return longest_len
