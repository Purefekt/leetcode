"""
Greedy with heap.
Always try to connect 2 smallest sticks into one, this way cost will be least.
Convert sticks into a heap and iterate over it till len(heap) < 2.
Take first 2, add that to the cost and add the sum back to the heap.

O(nlogn) time for the heap operations.
O(n) space for the heap.
"""

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heap = sticks
        heapq.heapify(heap)

        cost = 0
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            cost += first + second
            heapq.heappush(heap, first+second)
        
        return cost
