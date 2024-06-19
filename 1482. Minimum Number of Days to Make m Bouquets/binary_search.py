"""
Binary search over the days to find the least possible day.
l = min(bloomDay) and r = max(bloomDay).
Create a helper function to check if a given day is valid to form m bouquets.
Always try to group left most flowers, this will guarantee that we are using them optimally.
Binary search over days, for every valid(day) is True, update result and shift l = p-1; else r = p+1.

O(n*logd) where n is the size of bloomDay and d is the range of bloomDay.
O(1) space.
"""

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m*k > len(bloomDay):
            return -1

        l = min(bloomDay)
        r = max(bloomDay)

        def valid(day):
            total = 0
            adj = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    adj += 1
                else:
                    adj = 0
                
                if adj == k:
                    total += 1
                    adj = 0
                
                if total == m:
                    return True
            
            return False

        res = math.inf
        while l<=r:
            p = (l+r)//2

            if valid(p) is True:
                res = min(res, p)
                r = p-1
            else:
                l = p+1
        
        return res
