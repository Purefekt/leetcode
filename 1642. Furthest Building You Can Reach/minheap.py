"""
MinHeap.
We need to use ladders for the largest jumps and bricks for the smallest ones.
Create a pq which will store all the jumps where ladders were used.
Iterate through the heights, if no jump is needed, continue.
If a jump is needed, first try to use all ladders.
Once all ladders have been used, now add the next jump to the heap and pop to get the smallest jump.
Use bricks for this jump and thus decrement the bricks.
For heights = [4,12,2,7,3,18,20,3,19] and we have 2 ladders, when we get to the index 4, the pq = [8,5] and next jump is 15.
Now all ladders are used up. Add 15 to the pq to make [8,5,15] and pop to get 5. Now we know that till this index we must use ladders on [8,15] and use bricks for the jump with 5.

O(nlogn) time for the heap.
O(n) space for the heap.
"""

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        res = 0
        pq = []
        heapq.heapify(pq)
        for i in range(len(heights)-1):
            if heights[i] >= heights[i+1]:
                res += 1
                continue

            # use all ladders first
            if ladders > 0:
                heapq.heappush(pq, heights[i+1] - heights[i])
                ladders -= 1
                res += 1
            
            else:
                # get the smallest jump needed
                heapq.heappush(pq, heights[i+1] - heights[i])
                smallest_jump = heapq.heappop(pq)
                bricks -= smallest_jump
                if bricks < 0:
                    return res
                else:
                    res += 1
        
        return res
