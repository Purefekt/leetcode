"""
Sort the intervals. Now run a while loop and start with the first interval.
Save this intervals start and end times
Run a for loop from the current interval next interval till the last interval
keep updating the new end time if the current and next intervals overlap.
Move i to j so that we do not explore already merged intervals again.
Once we reach an interval which does not overlap, break the for loop and append the start and the updated end to res. Continue with next non merged interval
O(n) time to go over all intervals
O(logn) space to sort
""" 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        res = []
        i = 0
        while i < len(intervals):
            
            start_i = intervals[i][0]
            end_i = intervals[i][1]
            
            for j in range(i+1, len(intervals)):
                
                start_j = intervals[j][0]
                end_j = intervals[j][1]
                
                if end_i >= start_j:
                    end_i = max(end_i, end_j)
                    i = j
                else:
                    break
            
            res.append([start_i, end_i])
            
            i += 1
        
        return res
            