"""
Sort the intervals based on 2 things. First by the start point and then by the length. For example (1,4) comes before (1,2) when sorted
To do this, set the end point for each interval to its negation and then run sort, this will work since (1,-4) < (1,-2). Then negate it again to get the original values
Now begin with setting the start and end to the first interval and run through all the intervals from index 1 till the last
Each time an intervals start is greater than or eq to the start and end is less than or eq to the end, we will count that as an interval to remove.
At any point if this is not valid, we reset the start and end to the current interval's start and end
Solution will be total intervals - intervals to remove

O(nlogn) time. O(nlogn) time to sort and O(n) time to find all intervals to remove
O(n) space to sort in python
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        for i in range(len(intervals)):
            intervals[i][1] = -intervals[i][1]

        intervals.sort()

        for i in range(len(intervals)):
            intervals[i][1] = -intervals[i][1]

        start = intervals[0][0]
        end = intervals[0][1]

        rem = 0
        for i in range(1, len(intervals)):
            start_i = intervals[i][0]
            end_i = intervals[i][1]

            if start_i >= start and end_i <= end:
                rem += 1
            else:
                start = start_i
                end = end_i
        
        return len(intervals)-rem
