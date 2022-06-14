"""
convert the array into negative to use minheap as maxheap
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # negate all elements
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
            
        while len(stones) != 1:
            
            # get the two largest elements
            largest_stone_1 = heapq.heappop(stones)
            largest_stone_2 = heapq.heappop(stones)
                    
            if len(stones) == 0:
                return -(largest_stone_1 - largest_stone_2)
            
            if largest_stone_1 != largest_stone_2:
                rem_weight = largest_stone_1 - largest_stone_2
                heapq.heappush(stones, rem_weight)
        
        return -stones[0]
            