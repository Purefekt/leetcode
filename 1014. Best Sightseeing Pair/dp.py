"""
1d dp.
dp array tracks the best i values so far.
initialize it to an array with the first value of values.
Iterate over values from 1 till n.
First update result to max of res and current value + previous dp value - 1.
Update dp values to max of current val and previous dp value - 1 (since this value is 1 cell removed by moving further).

O(n) time to iterate over values once.
O(n) space used by dp array.
"""

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        dp = [values[0]]
        res = 0
        for i in range(1, len(values)):
            res = max(res, values[i] + dp[i-1] - 1)
            dp.append(max(values[i], dp[i-1]-1))
        
        return res
