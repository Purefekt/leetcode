"""
Top down DP.
For each questions, we can either take it or skip it.
If we skip it, then there is no change to points and we move on to the next question.
If we take it, then we need to skip the next brainpower_i number of questions and we get the points of that question.
Keep a memo table to maintain the max points of each index to reuse.
If the index is larger than or equal to length of questions, then return 0 points since we have exceeded the number of questions.

O(n) time to go through the array once.
O(n) space for stack
"""

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo = {}

        def helper(idx):
            if idx in memo:
                return memo[idx]
            if idx >= len(questions):
                return 0
            
            max_points = max(
                helper(idx+1), # skip
                helper(idx+1+questions[idx][1]) + questions[idx][0] # take
            )
            memo[idx] = max_points
            return max_points
        
        return helper(0)
        