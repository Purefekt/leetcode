"""
Greedy and sorting.
Get an array called minute reaches where each index belongs to a monster and what time that monster will reach the town. 
Time taken = distance / time.
Sort this to eliminate the monsters in the order they arrive to the town.
Now create a simulation from time=0 till number of monsters, if the current time is >= current monster's reach time, this means we cannot kill it and we lose, return.
"""

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        minuteReaches = []
        for i in range(len(dist)):
            minuteReaches.append(math.ceil(dist[i]/speed[i]))

        res = 0
        minuteReaches.sort()
        for i in range(len(minuteReaches)):
            if i >= minuteReaches[i]:
                return res
            res += 1
        
        return res
        