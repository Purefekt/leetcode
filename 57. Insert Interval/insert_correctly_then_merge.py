"""
Insert the element in its correct place in O(n) time. If the start of the new interval is less than the first interval start time, it must be added at the start.
If the start of the new interval is larger than the last interval start time, it must be added to the end
If the newInterval has to go somewhere in the end, then we can find the index where it must go and place it there
Once we have the interval, we run merge intervals to merge if there is any overlap

O(n) time since we run multiple linear passes
O(n) space to store new_intervals list
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new_intervals = []
        
        if not intervals:
            new_intervals.append(newInterval)
        else:
        
            start_new = newInterval[0]
            start_first = intervals[0][0]
            start_last = intervals[-1][0]

            # put the newInterval either at the start or the end or the middle
            if start_new < start_first:
                new_intervals.append(newInterval)
                new_intervals.extend(intervals)
            elif start_new > start_last:
                new_intervals.extend(intervals)
                new_intervals.append(newInterval)
            else:
                i = 0
                for i,interval in enumerate(intervals):
                    if interval[0] > start_new:
                        break
                for i in range(i):
                    new_intervals.append(intervals[i])
                new_intervals.append(newInterval)
                new_intervals.extend(intervals[i+1:])
        
        # run merge intervals
        start = new_intervals[0][0]
        end = new_intervals[0][1]
        res = []
        
        for j in range(1, len(new_intervals)):
            start_j = new_intervals[j][0]
            end_j = new_intervals[j][1]
            
            if end >= start_j:
                end = max(end, end_j)
            else:
                res.append([start,end])
                start = start_j
                end = end_j
        res.append([start,end])
        
        return res
        