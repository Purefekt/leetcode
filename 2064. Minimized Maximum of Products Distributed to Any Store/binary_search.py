"""
Binary search x.
Create a function which returns a boolean weather it is possible to distribute all products where max product given to any store is x.
Binary search over x in the range [1, max(quantities)], since we can simply assign the max val to each store and have a valid distribution.

O(nlogk) time where k is max(quantities). is_possible function runs in n time and the binary search portion runs for logk time.
O(1) space.
"""

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def is_possible(x):
            # we can give at max x to a given store
            stores = 0
            for q in quantities:
                stores += math.ceil(q/x)
                if stores > n:
                    return False
            return True
        
        # binary search for x
        res = max(quantities)
        l = 1
        r = max(quantities)

        while l<=r:
            x = (l+r)//2

            if is_possible(x) is True:
                res = x
                r = x-1
            else:
                l = x+1
        
        return res
