"""
Convert happiness into a max heap.
Keep track of number of iterations, we need to remove that much happiness from each next removal.
But do not go below 0.
Pop k times to get the res.

O(n + klogn) time since heapify take n time and heappop takes logn time which we do k times.
O(n) space used by the heap.
"""

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness = [-n for n in happiness]
        heapq.heapify(happiness)

        res = 0
        removed = 0
        for i in range(k):
            hap = -(heapq.heappop(happiness))
            hap -= removed
            res += max(hap, 0)
            removed += 1
        
        return res
