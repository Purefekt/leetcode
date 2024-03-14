"""
PrefixSum.
Keep a hashmap to track the number of occurances of a prefix sum.
Initialize it with {0:1} since we have 1 occurance of prefixsum 0 at the start.
Iterate through the array, first check if cur_sum - goal is in psum hashmap.
This would mean that there are those many arrays which can be removed from the array to create sum == goal.
Thus add that many to res.
Next increment the count of current psum in psum hashmap.

O(n) time to iterate over the array once.
O(n) space used by psum hashmap.
"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        res = 0
        psum = {0:1}

        cur_sum = 0
        for n in nums:
            cur_sum += n
            if cur_sum - goal in psum:
                res += psum[cur_sum - goal]
            if cur_sum not in psum:
                psum[cur_sum] = 1
            else:
                psum[cur_sum] += 1
        
        return res
