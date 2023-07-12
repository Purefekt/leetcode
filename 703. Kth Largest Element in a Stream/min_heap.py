"""
Create a heap with the initial array.
Pop all elements till this heap lenght == k. Now the first element of the heap is the kth largest.
Add an element to the heap and then pop an element from the heap.
The resulting element at heap[0] is the kth largest.
Edge case when the initial array is empty, so we have to check if size of array > k, only then pop.

O(n*log(n) + m*log(k)) time. O(n) to convert nums into a heap. O(nlogn) to get a heap of size k where k can be at max n. If there are M calls to add, and the size of our heap is at max k, each heappop is O(logk), thus add O(mlog(k))
O(n) space for heap.
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)