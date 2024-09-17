"""
Greedy.
Convert all times to minute integers and sort.
Get distance between each adjacent pair.
We also need distance between the 0th time and last time, since it will loop around.
Min distance between [00:00, 23:00, 23:59] is 1 minute since min distance is between 00:00 and 23:59.

O(nlogn) for sorting. Finding min time then takes linear time.
O(n) space for sorting and storing minutes.
"""

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        # reduce to mins
        mins = []
        for t in timePoints:
            h,m = t.split(':')
            minutes = int(h)*60 + int(m)
            mins.append(minutes)
        
        mins.sort()
        print(mins)
        # get the distance between each adjacent
        res = math.inf
        for i in range(len(mins)-1):
            diff = mins[i+1] - mins[i]
            res = min(res, diff)
        
        # also get the distance between 0th and last idx
        max_time = 24*60
        right_side = max_time - mins[-1]
        left_side = mins[0]
        edges_diff = right_side + left_side
        res = min(edges_diff, res)

        return res
