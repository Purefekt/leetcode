class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while(len(stones) != 1):
        
            two_largest = heapq.nlargest(2, stones)
            
            # if len of stones is 2, then return the diff of larger and smaller
            if len(stones) == 2:
                return two_largest[0] - two_largest[1]

            # if both numbers are equal, remove both elements from stones list
            if two_largest[0] == two_largest[1]:
                for i in range(len(stones)):
                    if two_largest[0] == stones[i]:
                        stones.pop(i)
                        break
                for i in range(len(stones)):
                    if two_largest[1] == stones[i]:
                        stones.pop(i)
                        break

            # if one is larger, remove both elements and add the diff of larger and smaller to the stones list
            else:
                remaining_stone = two_largest[0] - two_largest[1]
                for i in range(len(stones)):
                    if two_largest[0] == stones[i]:
                        stones.pop(i)
                        break
                for i in range(len(stones)):
                    if two_largest[1] == stones[i]:
                        stones.pop(i)
                        break

                stones.append(remaining_stone)
        
        return stones[0]
    