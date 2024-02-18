"""
Sort the meeting rooms.
Create a free_at array of size n, this array stores the free at time for each room.
Also creat a frequency hashmap to act as a counter for rooms.
Iterate through the meetings, for each meeting first check if it can be simply placed in a room.
For this, iterate over the rooms from 0 -> n and place a meeting in a room if its start time > that room's time. Also update the counter and the free_at time with the end time.
The other case is if the meeting cannot be placed simply, in this case get the first room which has the earliest free time.
Place this meeting in this room, the end time will now be shifted to earliest free time + duration.

O(mlogm + n*m) time for m meetings and n rooms. mlogm to sort and then outer loop to iterate through all meetings, and inner loop to iterate through all rooms.
O(n+m) space. m space for sorting the n space for the free_at and freq data structures.
"""

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        freq = {i:0 for i in range(n)}
        free_at = [0] * n

        for start, end in meetings:
            # check if we can place a meeting in any pos
            can_place = False
            for i in range(n):
                if free_at[i] <= start:
                    free_at[i] = end
                    freq[i] += 1
                    can_place = True
                    break
            
            if can_place is True:
                continue
            
            # otherwise get the earliest time and place the meeting there. The end time will be shifted
            earliest_free = min(free_at)
            earliest_idx = free_at.index(earliest_free)
            free_at[earliest_idx] = earliest_free + (end-start)
            freq[earliest_idx] += 1

        
        res_val = max(freq.values())
        for i in range(n):
            if freq[i] == res_val:
                return i
        