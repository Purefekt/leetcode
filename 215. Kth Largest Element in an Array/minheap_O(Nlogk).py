"""
Using min heap. Convert all nums to negative and then loop over and pop the min heap k times. The last popped will be the kth largest. 

O(Nlogk)
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # flip the sign of all num in nums
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        # create priority queue of nums
        heapq.heapify(nums)
        
        for i in range(k):
            out = heapq.heappop(nums)
        
        return -out
    