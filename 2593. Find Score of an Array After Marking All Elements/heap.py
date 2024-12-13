"""
Heap.
Store the num, index into a heap.
Maintain a set for all marked indexes.
Pop from heap, add to result if this index was not seen.
Also add it to marked indexes set along with its prev and next indexes.

O(nlogn) time for heap functions.
O(n) space used by marked indexes set and heap.
"""

class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        pq = []
        heapq.heapify(pq)
        marked_idx = set()
        for i,n in enumerate(nums):
            heapq.heappush(pq, (n, i))
        
        res = 0
        while pq:
            score, idx = heapq.heappop(pq)
            if idx not in marked_idx:
                res += score
                marked_idx.add(idx)
                marked_idx.add(idx-1)
                marked_idx.add(idx+1)
        
        return res
