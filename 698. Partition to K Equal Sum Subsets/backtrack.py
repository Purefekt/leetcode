"""
Backtracking.
We can have k buckets and try to place each num into one of k buckets.
This will be k^n time, since the tree will have height n and k options at each level.
We could instead try to fill find k groups one by one.
During finding 1 group, we choose either to keep or skip current number to be a part of this group.
To find each group, the time complexity if 2^n and we repeat this k times.

O(k*2^n) time.
O(n) space.
"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums)//k
        # array to track if this number is available to be used
        avail = [True] * len(nums)
        # optimization prune early
        nums.sort(reverse = True)

        def backtrack(k_remaining, idx, cur_sum):
            if k_remaining == 0:
                return True
            if cur_sum == target:
                return backtrack(k_remaining-1, 0, 0)
            
            for j in range(idx, len(nums)):
                # skip if current number is already used or if it cannot be added to this group
                if not avail[j] or cur_sum + nums[j] > target:
                    continue
                
                # use this num in current group
                avail[j] = False
                if backtrack(k_remaining, j+1, cur_sum + nums[j]) is True:
                    return True
                avail[j] = True

                # prune
                if cur_sum == 0:
                    return False
            
            return False
        
        return backtrack(k, 0, 0 )
