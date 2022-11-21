"""
Sort the intervals. We need to compare two adjacent intervals and see if there needs to be a deletion
Start with keeping track of the ending of the first intervals
Run a loop from the 2nd interval till the end
If the start of the 2nd interval is smaller than end of first, this means there is an overlap, we increase result by 1
This would mean we have to delete one of the two intervals. We must delete the one with the higher end time, since that will have more chances to overlap with other intervals. So set the end_first to min of end_first and end_second
If there is no overlap, then simply set the end_first to end_second since the intervals are sorted and if there is no overlap, the end of the 2nd interval will always be larger than the 1st. 

O(nlogn) time. O(n) to go over all intervals and O(nlogn) to sort
O(n) space complexity due to sorting
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        res = 0
        
        end_first = intervals[0][1]
        for i in range(1, len(intervals)):
            start_second, end_second = intervals[i]
            
            # if there is an overlap, increase count by 1 and set the end_first to the end of the non deleted interval
            if start_second < end_first:
                res += 1
                end_first = min(end_first, end_second)
            
            # else no overlap, this means end_first becomes end_second
            else:
                end_first = end_second
        
        return res
        