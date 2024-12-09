"""
Break the array into continuous segments where each segment is true.
And the segments break where they would be false.
Store the indexes and which array they belong to in a hashmap.
Then go over the queries and both start and ends must be in the same array group to be true.

O(n) time to create the index to array mapping and then one pass over queries.
O(n) space to store mapping of each index to array.
"""

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        # separate array into multiple correct arrays
        cur = None
        idx_to_arr = {}
        arr_count = 0

        for i,n in enumerate(nums):
            if not cur:
                if n%2 == 0:
                    cur = 'even'
                else:
                    cur = 'odd'
                idx_to_arr[i] = arr_count
            else:
                # case where we break the array
                if (cur == 'even' and n%2 == 0) or (cur == 'odd' and n%2 == 1):
                    arr_count += 1
                    if n%2 == 0:
                        cur = 'even'
                    else:
                        cur = 'odd'
                    idx_to_arr[i] = arr_count
                else:
                    idx_to_arr[i] = arr_count
                    if cur == 'even':
                        cur = 'odd'
                    else:
                        cur = 'even'
        
        # for a query to be true, both start and end must be in the same array group
        res = []
        for s,e in queries:
            if idx_to_arr[s] == idx_to_arr[e]:
                res.append(True)
            else:
                res.append(False)
        
        return res
