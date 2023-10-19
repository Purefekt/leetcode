"""
Binary search to find the minimum capacity.
The least capacity we must have is the max value of any individual weight.
The max capacity we can have is the sum of all weights, and that will allow us to do it in 1 day, but this might not be optimal.
This is the search space, start binary search.
For each capacity being tested (midpoint), iterate through the days and count number of days needed.
Increment number of days needed when a certain batch of weights > capacity.
At the end of iteration, if the number of days is <= days, then update result to it and shift r = midpoint - 1. This is because even tho the capacity we found was valid, we can still find a smaller capacity which is also valid.
If the number of days > days, then this is invalid and we shift l = midpoint + 1.

O(nlogm) time where n is length of weights and m is the sum of weights, since binary search will be over this.
O(1) space 
"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)

        res = 0
        while l<=r:
            capacity = (l+r)//2

            num_days_needed = 0
            cur_weight = 0
            for i in range(len(weights)):
                cur_weight += weights[i]
                if cur_weight > capacity:
                    num_days_needed += 1
                    cur_weight = weights[i]
            num_days_needed += 1

            if num_days_needed <= days:
                res = capacity
                r = capacity - 1
            else:
                l = capacity + 1
        
        return res
