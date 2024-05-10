"""
Get all possible pairs and put them in an array with the following format: [arr[i]/arr[j], [arr[i], arr[j]]].
Heapify this.
Pop k-1 times.
Result is at the top.

O(klog(n^2)) time. Heapify takes n^2 time. Each heappop takes log(n^2) time and we do it k times.
O(n) space used by the heap.
"""

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        # get all fractions
        fractions = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                fractions.append([arr[i]/arr[j], [arr[i], arr[j]]])
        
        heapq.heapify(fractions)
        for _ in range(k-1):
            heapq.heappop(fractions)
        
        return fractions[0][1]
