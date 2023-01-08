"""
Backtracking with memoization
For each index, we can either add it or substract it, giving 2 decisions, brute force will be to go over the entire decision tree
Use a cache hashmap called dp.
Recursive function takes the current sum and index, base case would be if (sum,index) is already in the cache then return from cache table
Base case if we reach the end, we check if the summ is target, if yes then return 1 else 0.
For each (sum,idx), its value will be the sum of + and - sides

O(t*n) time. where t is the sum of array and n is len of array. 
O(t*n) space
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:



        dp = {}
        def backtrack(summ, idx):

            if (summ,idx) in dp:
                return dp[(summ,idx)]

            if idx == len(nums):
                if summ == target:
                    return 1
                else:
                    return 0
                return
            
            dp[summ,idx] = backtrack(summ+nums[idx], idx+1) + backtrack(summ-nums[idx], idx+1)
            
            return dp[(summ, idx)]
        
        backtrack(0,0)

        return dp[(0,0)]
        