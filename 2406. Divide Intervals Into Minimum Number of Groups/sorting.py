"""
Same as meeting rooms 2.
Get array of starts and ends and sort separately.
Maintain pointers at start of both starts and ends.
If num at start pointer is <= num at end pointer, increment cur by 1.
Else decrement cur by 1.
Track the largest cur value. This will be the max number of groups we need at once.

O(nlogn) time. nlogn for sorting and then n time to run through.
O(n) space used by starts and ends arrays and sorting.
"""

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        starts = [s for s,e in intervals]
        ends = [e for s,e in intervals]
        starts.sort()
        ends.sort()

        p1 = 0
        p2 = 0
        res = 0
        cur = 0

        while p1<len(starts):
            if starts[p1] <= ends[p2]:
                cur += 1
                res = max(res, cur)
                p1 += 1
            else:
                cur -= 1
                p2 += 1
        
        return res