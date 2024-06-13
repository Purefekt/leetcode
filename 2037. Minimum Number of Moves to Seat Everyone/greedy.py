"""
Greedy sort.
Sort both arrays and for each index, sum the absolute diff.
This is because the closest seat to any student will be the lowest number after sorting.

O(nlogn) time.
O(n) space.
"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()

        res = 0
        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        
        return res
