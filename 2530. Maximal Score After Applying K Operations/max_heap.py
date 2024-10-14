"""
Heap.
Create a maxheap from nums.
Pop largest num, add to nums and return the changed val ie val/3 to nums.

O(klogn + n) time since creating the heap takes n time and each heap operation takes logn time which we run k times.
O(n) space used by heap.
"""

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = 0
        for _ in range(k):
            val = abs(heapq.heappop(nums))
            res += val
            new_val = math.ceil(val/3)
            heapq.heappush(nums, -new_val)
        
        return res
