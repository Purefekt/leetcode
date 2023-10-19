"""
Recursion with memoization.
Keep adding each number in nums to current sum and backtrack to try different values.
Can cache the cur_sum in a memoization table.

O(t*n) where t is target and n is len of nums. Helper can be called t times and each time has a loop of size n.
O(t) space for stack which is the size of recursion stack of t.
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def helper(cur_sum):
            # cache hit
            if cur_sum in memo:
                return memo[cur_sum]
            
            # base case
            if cur_sum >= target:
                if cur_sum == target:
                    return 1
                else:
                    return 0
            
            res = 0
            for n in nums:
                cur_sum += n
                res += helper(cur_sum)
                # backtrack
                cur_sum -= n
            
            memo[cur_sum] = res
            return res
        
        return helper(0)
