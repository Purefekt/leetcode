"""
Greedy.
Remove numbers with lower frequency.
Create a minheap with (frequency, integer).

O(nlogn) time for minheap. 
O(n) space used by heap.
"""

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        counter = collections.defaultdict(int)

        for n in arr:
            counter[n] += 1
        
        pq = []
        for key,val in counter.items():
            pq.append((val,key))
        heapq.heapify(pq)

        while pq and k>0:
            val, key = heapq.heappop(pq)
            k -= val
            if k < 0:
                return len(pq)+1
        
        return len(pq)
