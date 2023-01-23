"""
Like merged intervals. We consider the coordinates as intervals and merge them
But we update the end to be the min(end, end_j), this is because we might have intervals (1,6) (2,8) (7,12); if we merge them then we get (1,12), but we actually need 2 arrows for these intervals,
thus we get the intervals (1,8) (7,12) after merging with min end

O(nlogn) time. O(nlogn) to sort and O(n) to go through all intervals in one pass
O(n) to sort
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()

        start = points[0][0]
        end = points[0][1]

        count = 1
        for j in range(1, len(points)):
            start_j ,end_j = points[j]

            if end >= start_j:
                end = min(end, end_j)
            
            else:
                count += 1
                start = start_j
                end = end_j
        
        return count
