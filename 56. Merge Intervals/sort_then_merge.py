"""
Sort the interval list. Then take two pairs at a time and see if they are overlapping. If they are then merge and add the new merged interval to output and go to the next 2 pairs by jumping 2 indices.
If they do not overlap then move to next to pairs where the 2nd element of the previous pair is now the first element of the new pairs. Add the first element of the prev pair to the output list.
Repeat this till there are no more overlapping pairs, use a flag to detect this.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # edge case where there is only 1 interval
        if len(intervals) < 2:
            return intervals
    
        # sort intervals
        intervals.sort()
        
        output, flag = self.merge_helper(intervals)        
        while flag != 0:
            output, flag = self.merge_helper(output)
        
        return output
     
    def merge_helper(self, intervals):      
        flag = 0
        output = []
        p1 = 0
        p2 = 1
        while p1 < len(intervals)-1:
            if intervals[p1][1] >= intervals[p2][0]:
                output.append([min(intervals[p1][0], intervals[p2][0]), max(intervals[p1][1], intervals[p2][1])])
                flag = 1
                p1 += 2
                p2 += 2
            else:
                output.append(intervals[p1])
                p1 += 1
                p2 += 1
        # add the last element
        if p1<len(intervals):
            output.append(intervals[p1])
        return output, flag
    