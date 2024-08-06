"""
MaxHeap.
Create a maxheap of counter of all chars.
Pop from maxheap and assign chars to first 8 distinct numbers 2-9.
Then repeat by reassigning from 2-9, this time each use of this char takes 2x the clicks.
Repeat for 3rd round and 4th as well.

O(n) time to create counter hashmap and maxheap. We iterate till maxheap and pop each time which takes O(klogk) time where k=26 thus is constant time operation.
O(1) space since size of hashmap and heap will be at max O(26).
"""

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        # create maxheap of counters of all chars
        counter = collections.defaultdict(int)
        for c in word:
            counter[c] += 1
        
        max_heap = []
        for k,v in counter.items():
            max_heap.append((-v, k))
        heapq.heapify(max_heap)

        # pop chars from maxheap and assign to first 8 numbers (2-9) and then repeat
        res = 0
        i = 0
        while max_heap:
            val, char = heapq.heappop(max_heap)
            val *= -1
            factor = (i//8)+1
            res += (val*factor)
            i += 1
        
        return res
