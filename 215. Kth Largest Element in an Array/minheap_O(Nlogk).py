"""
Heap
Multiply all elements by negative to convert min heap functionality to max heap
Heapify the list
pop k times, the last popped element will be -result

O(nlogk) time
O(k) space to store heap elements
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)
        
        res = 0
        for i in range(k):
            res = heapq.heappop(nums)
        
        return -res
    