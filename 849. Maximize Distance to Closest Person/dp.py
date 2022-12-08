"""
Dynamic programming.
A dp array of len(seats) to store left_dp, one to store right_dp and one to store final dp
For every position where there is a seat, the pos in left_dp and right_dp will be 0
if the first seat is empty, then we fill it with 0 in left_dp and if the last seat is empty then we fill it with 0 in right_dp
We fill the left_dp from left to right, if the prev seat was 1, then set it to 1, if the prev left_dp was 0, fill it with 0, else fill it with prev left_dp + 1
Same for right_dp but we fill from right to left
Final_dp will have its first and last element as max(left_dp, right_dp) for those positions. The remaining elements will be min(left_dp,right_dp)
Result will be max element of final_dp array.

O(n) time for multiple linear passes over the seats array
O(n) space to store left, right and final dp arrays
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        left_dp = [None for _ in range(len(seats))]
        right_dp = [None for _ in range(len(seats))]

        for i in range(len(seats)):
            if seats[i] == 1:
                left_dp[i] = 0
                right_dp[i] = 0
        
        # initialize left and right dp arrays
        if seats[0] == 0:
            left_dp[0] = 0
        if seats[-1] == 0:
            right_dp[-1] = 0
        
        # fill left_dp
        for i in range(1,len(seats)):
            if seats[i] == 0:
                if seats[i-1] == 1:
                    left_dp[i] = 1
                elif left_dp[i-1] == 0:
                    left_dp[i] = 0
                else:
                    left_dp[i] = left_dp[i-1] + 1
        
        # fill the right_dp
        for i in range(len(seats)-2,-1,-1):
            if seats[i] == 0:
                if seats[i+1] == 1:
                    right_dp[i] = 1
                elif right_dp[i+1] == 0:
                    right_dp[i] = 0
                else:
                    right_dp[i] = right_dp[i+1] + 1
        
        final_dp = [0 for _ in range(len(seats))]
        final_dp[0] = max(left_dp[0], right_dp[0])
        final_dp[-1] = max(left_dp[-1], right_dp[-1])
        for i in range(1,len(final_dp)-1):
            final_dp[i] = min(left_dp[i], right_dp[i])
        
        return max(final_dp)
