"""
Sort the intervals based on start time. Then for each pairs of adjacent intervals check if the 2nd intervals start time if after the first intervals end time. If not then false, if all are fine then true.
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        pointer = 0
        while pointer < len(intervals)-1:
            if intervals[pointer][1] > intervals[pointer+1][0]:
                return False
            pointer += 1
        
        return True
         