"""
Backtracking.
Helper function takes idx and combo.
At each idx, we can either keep in in the combo or skip it.
But we can only keep it if nums[idx] and any other val in the combo are not k diff.
Return res-1 since our function considers the empty arr [] as well.

O(n*2^n) time since we run helper for 2^n times and in half of those we need to go through current combo arr to determine if we can add it to combo.
O(n) space since the max height of tree or the call stack will be of size n.
"""

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def valid(arr, val):
            for n in arr:
                if abs(n-val) == k:
                    return False
            return True

        def helper(idx, combo):
            if idx == len(nums):
                return 1
            
            res = 0
            # keep
            if valid(combo, nums[idx]) is True:
                combo.append(nums[idx])
                res += helper(idx+1, combo)
                combo.pop()
            
            # skip
            res += helper(idx+1, combo)
            return res
        
        return helper(0, [])-1
