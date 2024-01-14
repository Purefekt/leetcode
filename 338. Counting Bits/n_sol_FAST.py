"""
1d DP.
Write down the binary rep from 0 -> 8 and see a pattern.
Number of ones in 0 is 0, number of ones in 1 is 1.
Number of ones in 2 is 1 + number of ones in 0. Number of ones in 3 is 1 + number of ones in 1.
Number of ones in 4 is 1 + number of ones in 0. Number of ones in 8 is 1 + number of ones in 0.
Till every power of 2, the number of ones is 1 - dp[i - current power of 2].
The current power is offset, thus set up the dp array as [0,1].
Then iterate from 2 till n+1, first update the offset.
If offset * 2 == i, we have a new offset = i.
Append 1 + dp[i-offset] as the number of ones for the ith number.

O(n) time.
O(1) space since the dp array is the output.
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0, 1]

        if n < 2:
            return dp[:n+1]
        
        offset = 2
        for i in range(2, n+1):
            # update offset
            if offset * 2 == i:
                offset = i
            
            dp.append(1 + dp[i-offset])
        
        return dp
