# initialize a min heap. Remove the smallest element from this min heap till the size of this min heap == k
# on every add call, add the element to the heap and remove the min element once. The new min element will be the kth largest
# but if the initial heap was empty, add a check to see if len of heap == k

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        heapq.heapify(self.heap)
        
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)      

    def add(self, val: int) -> int:
        # add the element to the heap maintaining the heap property
        heapq.heappush(self.heap, val)
        
        # most cases
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
            return self.heap[0]
        else:
            return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)