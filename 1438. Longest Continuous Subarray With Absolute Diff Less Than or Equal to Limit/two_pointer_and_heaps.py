"""
Sliding window with 2 heaps.
We can use a sliding window to check for a subarray and use a maxheap and minheap to track the max seen and min seen number.
set left to 0 and iterate right from 0 till n.
Push nums[r] and r (index) to maxheap and minheap.
First adjust left to keep it valid, to do this, check if the current max-min > limit.
If it is, then we must shift left.
To shift left, we can get the best earliest index we can shift to by getting min(max_heap index, min_heap index).
After doing this, we need to eject all elements from the heap which are now out of the range ie left of left pointer.
Update result.

O(nlogn) time. Iterate over array n while moving r pointer. Inside it, we push and pop from both heaps at most once which takes logn time.
O(n) space used by the heaps.
"""

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        max_heap = []
        min_heap = []
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)
        res = 0
        l = 0

        for r in range(len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            heapq.heappush(min_heap, (nums[r], r))

            # correct left bound
            while -max_heap[0][0] - min_heap[0][0] > limit:
                l = min(max_heap[0][1], min_heap[0][1]) + 1

                # remove numbers which fall out of range after updating l
                while max_heap[0][1] < l:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < l:
                    heapq.heappop(min_heap)
            
            res = max(res, r-l+1)
        
        return res
