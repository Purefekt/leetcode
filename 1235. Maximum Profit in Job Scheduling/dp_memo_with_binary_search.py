"""
Dp with memoization and binary search.
Sort the intervals by start time.
Create a recursive function which takes the idx, that means the current interval we are at. 
We can either keep this interval or we can discard it.
If we keep this interval, then we pass the next valid interval to the recursive function.
Next valid interval is the one which has its start time >= end time of currently chosen interval.
We use binary search to find this interval in logn time.
To skip the interval, simply move to the next index.
Return the max of keep and skip cases.
Base case is when idx == len(startTime), we return 0.
Use memoization on the idx to cache values.

O(nlogn) time, the recursive function runs in linear time and inside each run, we do binary search again on length n.
O(n) space to store the memoization table.
"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        combined = []
        for i in range(len(startTime)):
            combined.append((startTime[i], endTime[i], profit[i]))
        combined.sort()

        # store startTimes as a 1d array for easier binary search
        startTime = []
        for n in combined:
            startTime.append(n[0])
        
        # return the closest number which is larger than target.
        def binary_search(l, target):
            r = len(startTime)
            closest = len(startTime)
            while l<r:
                p = (l+r)//2
                if startTime[p] >= target:
                    r = p
                else:
                    l = p+1
            return r


        memo = {}
        def helper(idx):

            if idx in memo:
                return memo[idx]

            if idx == len(combined):
                return 0
            
            # keep this interval, get the next valid interval whose start >= end_current using Binary search
            start_current, end_current, profit_current = combined[idx]
            next_idx = binary_search(idx+1, end_current)
            keep = profit_current + helper(next_idx)

            # skip this interval
            skip = helper(idx+1)

            memo[idx] = max(keep, skip)
            return max(keep, skip)
        
        return helper(0)
