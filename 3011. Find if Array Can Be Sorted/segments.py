"""
For any array of numbers where all nums have the same set bit, we can keep swapping adj nums to always sort this array.
Divide the subarays into segments of same bits.
So [8,4,2,30,15] becomes [[8,4,2],[30,15]].
Now we compare adj segments, the max of ith segment must be smaller than min of i+1st segment.

O(n^2) time since creating segments takes n time and then iterating through n-1 segments takes n-1 time but we need to get min and max for each which takes another n time.
O(n) space used by segments.
"""

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        # create continguous segments of same set bits
        segments = []
        cur_count = 0
        cur_seg = []
        for n in nums:
            count = 0
            for c in bin(n)[2:]:
                if c == '1':
                    count += 1
            if count == cur_count:
                cur_seg.append(n)
            else:
                segments.append(cur_seg)
                cur_count = count
                cur_seg = [n]
        segments.append(cur_seg)

        # remove the initial empty segments
        segments = segments[1:]

        # the max num of ith segment must be smaller than min num of i+1st segment
        for i in range(len(segments)-1):
            if max(segments[i]) >= min(segments[i+1]):
                return False
        
        return True
