"""
DP.
At each day, we can choose to take a daily ticket or a weekly or a monthly.
If we are at a day whose ticket is already paid for, we continue to the next day.
Track an integer for the last day for which ticket is paid for.

O(n) time. days paid will be fixed 365.
O(n) space used by stack and memo table.
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        memo = {}
        def helper(idx, days_paid):
            if (idx, days_paid) in memo:
                return memo[(idx, days_paid)]
            if idx == len(days):
                return 0
            
            # skip this day if already paid for
            res = 0
            if days[idx] <= days_paid:
                res = helper(idx+1, days_paid)
            else:
                daily = costs[0] + helper(idx+1, days[idx])
                weekly = costs[1] + helper(idx+1, days[idx] + 6)
                monthly = costs[2] + helper(idx+1, days[idx] + 29)
                res = min(daily, weekly, monthly)
            
            memo[(idx, days_paid)] = res
            return res
        
        return helper(0, 0)