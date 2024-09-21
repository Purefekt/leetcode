"""
We can only use a triplet if all 3 values are <= to all three corresponding values in target.
And actually we only care about this triplet if atleast 1 of the 3 values is equal to 1 of the three values in target.
Set 3 flags to false: a,b,c.
Iterate through the flags, first check that each element is <= the corresponding element in target.
Now we can consider this triplet.
Now if any of a,b,c are == target, then set those as True.
Finally return a and b and c.

O(n) time.
O(1) space.
"""

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a = False
        b = False
        c = False

        for ta,tb,tc in triplets:
            # only accept this triplet if all values are <= target
            if ta <= target[0] and tb <= target[1] and tc <= target[2]:
                if ta == target[0]:
                    a = True
                if tb == target[1]:
                    b = True
                if tc == target[2]:
                    c = True
        
        return a and b and c
