"""
Binary search.
We binary search over the max number of balls.
Min at 1 and max at max(nums).
Set a max balls value and try to see if its possible to achieve that with max operations.
To split a bag, we use math.ceil(bag size / max balls) - 1.
So if max balls is 5 and bag size is 17, we split it with 3 moves.
But if bag size < max balls, we do not use any moves.

O(nlogm) time where n is size of nums and m is search space.
O(1) space.
"""

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        l = 1
        r = max(nums)

        def is_valid(max_balls):
            # try to break each current bag into bags with at max max balls and see if it is possible
            moves = 0
            for n in nums:
                if n < max_balls:
                    continue
                moves += (math.ceil(n/max_balls)-1)
                if moves > maxOperations:
                    return False
            return True

        res = r
        while l<=r:
            max_balls = (l+r)//2

            if is_valid(max_balls) is True:
                res = max_balls
                r = max_balls - 1
            else:
                l = max_balls + 1
        
        return res
