"""
Heap.
For any prefix sum ending at index r, we need to see if we can remove a prefixsum from left side which would still be >= k.
If we have [-1,2,-1,2,3], the psum at index 3 is 2. The psum at index 0 is -1.
If we remove the psum at index 0 for a window that ends at index 3, then we get 2 - (-1) => 3.
We use a minheap to track the smallest psum and its index.
Iterate over nums, increment the psum.
Then try to reduce the window by popping all psums from left till it can be done.
Note that this approach does not consider every possible subarray but it only skips the ones which would never be the result so that is why it works.

O(nlogn) time since we iterate over nums and for each iteration, we use the heap.
O(n) space used by the heap.
"""

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        res = math.inf

        cur_psum = 0
        # (psum, end_idx)
        pq = []

        for r in range(len(nums)):
            cur_psum += nums[r]

            if cur_psum >= k:
                res = min(res, r+1)
            
            # find the smallest window ending at r
            while pq and cur_psum - pq[0][0] >= k:
                psum, end_idx = heapq.heappop(pq)
                res = min(res, r-end_idx)
            
            heapq.heappush(pq, (cur_psum, r))
        
        if res == math.inf:
            return -1
        return res
