"""
2 Heaps.
Maintain 2 heaps which maintain 2 properties.
They can never have a size difference of more than 1 and all elements in heap1 must be smaller than all elements in heap2.
To do this, initialize 2 heaps and call them small and large.
Small has all numbers less than all numbers in large. Small is a maxheap and large is a minheap.
At first if small is empty, simply add the - of current number to it (for maxheap property).
Next check, if the current number is < abs(small[0]), in other words if current number is smaller than the largest in small, then add that number to small heap. Else add it to large heap.
After adding, we need to balance, balance only when |len(small) - len(large)| > 1.
To balance, if small has more numbers, sent its maximum to large heap, maximum is simply at the first pop. Similary if large has more numbers, send its minimum to small heap, which is at first pop.
In find median, if sum of lengths of both is even, then return (small[0] + large[0])/2. If it is odd then return the top element in the heap with more numbers.

O(logn) time to addNum each time it is called. O(1) time for findMedian.
O(n) space to maintain heaps.
"""

class MedianFinder:

    def __init__(self):
        # maxheap
        self.small = []
        # minheap
        self.large = []
        heapq.heapify(self.small)
        heapq.heapify(self.large)
        

    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush(self.small, -num)
        else:
            if num < abs(self.small[0]):
                heapq.heappush(self.small, -num)
            else:
                heapq.heappush(self.large, num)
        
        # balance if needed
        if abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) > len(self.large):
                to_move = -heapq.heappop(self.small)
                heapq.heappush(self.large, to_move)
            else:
                to_move = -heapq.heappop(self.large)
                heapq.heappush(self.small, to_move)
        

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 0:
            left = -self.small[0]
            right = self.large[0]
            return (left + right)/2
        else:
            if len(self.small) > len(self.large):
                return -self.small[0]
            else:
                return self.large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()