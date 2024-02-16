"""
Linear scan. Go through the intervals in order and for each determine how it is added to the result.
An interval ca be completely added if no overlap exists.
An interval can be split into 2 if it completely overlaps with toBeRemoved and it is longer.
An interval can be skipped if it completely overlaps with toBeRemoved and it is smaller.
An interval can have valid portion on left by overlapping on the right end.
An interval can have valid portion on the right by overlapping on the left end.

O(n) time for linear scan.
O(1) space.
"""

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        res = []
        for i in range(len(intervals)):
            start_i, end_i = intervals[i]

            # no overlap
            if start_i >= toBeRemoved[1] or end_i < toBeRemoved[0]:
                res.append((start_i, end_i))
            
            # overlap
            else:
                # complete overlap by toberemoved
                if start_i >= toBeRemoved[0] and end_i <= toBeRemoved[1]:
                    continue
                # complete overlap by interval, leads to 2 intervals
                elif start_i < toBeRemoved[0] and end_i > toBeRemoved[1]:
                    res.append((start_i, toBeRemoved[0]))
                    res.append((toBeRemoved[1], end_i))
                # left portion is valid
                elif start_i < toBeRemoved[0] and end_i > toBeRemoved[0]:
                    res.append((start_i, toBeRemoved[0]))
                # right portion is valid
                else:
                    res.append((toBeRemoved[1], end_i))
        
        return res
