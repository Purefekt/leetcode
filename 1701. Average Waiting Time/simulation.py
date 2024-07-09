"""
Simulation.

O(n) time for one pass over customers.
O(1) space.
"""

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        cur = 0
        res = 0
        for i in range(len(customers)):
            cur = max(cur, customers[i][0])
            nextt = cur + customers[i][1]
            res += nextt - customers[i][0]
            cur = nextt
        
        return res/len(customers)
