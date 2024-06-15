"""
Sorting and heapq.
At a given w value, we can choose from all profits which require upto and including w capital.
Suppose we have profits = [4,3,2,5,3,4,6,2] and capital = [0,0,0,1,1,1,2,2].
If we sort both with capital (it is already sorted), we know that if w = 0, our options are [4,3,2] and if w = 1 our options are [4,3,2,5,3,4].
After sorting initialize a heap called options.
Run a loop till k, inside this loop, we first need to update options as a maxheap.
To do this, have a pointer to the index of capital till where we have already considered these profits in options.
Include all profits which are <= current w.
Then take 1 (max value) from this maxheap.

O(k*nlogn) time since we need nlogn time to sort and the outer loop runs k times, inside we run n times for idx and we do a heappush operation each time.
O(n) space used by sorting and heap.
"""

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        cap_profits = []
        for i in range(len(profits)):
            cap_profits.append((capital[i], profits[i]))
        cap_profits.sort()
        capital = []
        profits = []
        for c,p in cap_profits:
            capital.append(c)
            profits.append(p)
        
        options = []
        heapq.heapify(options)
        idx = 0
        for _ in range(k):
            # update options with all profits which current w can use. Use maxheap
            while idx<len(capital) and capital[idx]<=w:
                heapq.heappush(options, -profits[idx])
                idx += 1
            
            # take 1 from heap. If it doesnt exists that means there arent any more options so exit
            if options:
                w -= heapq.heappop(options)
            else:
                break
        
        return w
