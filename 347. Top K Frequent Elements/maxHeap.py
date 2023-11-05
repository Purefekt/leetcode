"""
MaxHeap.
Create a frequency hashmap in O(n) time.
Then use that to create a maxHeap in O(n) time since heapify is O(n) operation.
Now pop k times to get the k highest frequency elements in O(klogn) time.
This is faster than nlogn if k<n. So if k==n then simply return nums in O(1) time.

O(klogn) time.
O(n+k) space. n space for hashmap and k space for heap.
""" 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # O(1) solution if k==n
        if k == len(nums):
            return nums
        
        # build the freq hashmap in O(n) time
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        # build maxHeap in O(n) time
        maxHeap = []
        for key,val in freq.items():
            maxHeap.append((-val, key))
        heapq.heapify(maxHeap)

        # pop the k most frequent elements in O(klogn) time
        res = []
        for _ in range(k):
            frequency, number = heapq.heappop(maxHeap)
            res.append(number)
        
        return res
