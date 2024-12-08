"""
Heapq.
Greedy approach, sort events by start time.
Add (end time, value) to heap.
For any new event, first remove all events which have concluded properly.
That is the current event's start time < prev event's end time.
We track the max current seen value, use this value with current event's value to update result.
This is because an event which has already concluded, can be paired with ANY future events.

O(nlogn) time since we iterate over all events and heap operations take logn time.
O(n) space to hold the pq.
"""

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        pq = []
        heapq.heapify(pq)

        res = 0
        max_seen = 0
        for s,e,v in events:
            while pq and pq[0][0] < s:
                _, prev_v = heapq.heappop(pq)
                max_seen = max(max_seen, prev_v)

            res = max(res, max_seen + v)
            heapq.heappush(pq, (e,v))
        
        return res
