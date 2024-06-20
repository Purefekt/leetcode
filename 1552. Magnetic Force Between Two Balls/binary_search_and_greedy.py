"""
Greedy and binary search.
We can binary search over the search space force, l = 1 and r = max(position).
For a given force value, we can check if it satisfies the condition to allow m balls with atleast force.
Atleast is important, we are NOT checking for exactly force amount.
To check, we can sort the positions array and iterate over it, placing a ball if the distance to previously placed ball is >= force.
Return true if balls placed == m.

O(nlogn + nlogk) time since nlogn time to sort postions array. We run binary search for logk times and each time do a search over positions which takes n time.
O(n) space used for sorting.
"""

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        l = 1
        r = position[-1]

        def valid(f):
            # set first ball to position[0]
            prev_pos = position[0]
            balls_placed = 1
            for i in range(1, len(position)):
                if position[i] - prev_pos >= f:
                    prev_pos = position[i]
                    balls_placed += 1
                if balls_placed == m:
                    return True
            return False

        res = 0
        while l<=r:
            force = (l+r)//2
            if valid(force) is True:
                res = force
                l = force+1
            else:
                r = force-1
        
        return res
