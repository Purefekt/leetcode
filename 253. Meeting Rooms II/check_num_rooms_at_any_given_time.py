"""
For every time, keep a track of how many rooms we need at THAT time. Keep a track of max number of rooms during the entire time
For this store all start times and end times in separate arrays and sort both.
Use 2 pointers, one for start and one for end and loop till we reach the end of all start times.
If the start time is smaller than the pointer at end time, we add one room to the count (and update max_count)
If the start time is less than or equal to an end time, decrease count by 1 cos this means a meeting has ended and a room is free.
O(nlogn) to sort both arrays and then O(n) to traverse thus O(nlogn)
O(n) space to store both arrays
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        starts.sort()
        ends.sort()

        ps, pe = 0, 0
        count = 0
        max_count = 0
        while ps < len(starts):
            if starts[ps] < ends[pe]:
                count += 1
                max_count = max(max_count, count)
                ps += 1
            else:
                count -= 1
                pe += 1
        
        return max_count
    