"""
Greedy, sort the peoples weight and use 2 pointers
l at 0 and r at len(people)-1. If the combined sum of the heaviest and lightest people is <= limit, move both pointers and increment res
Else increment res and decrement r pointer since we give 1 boat to the heaviest person. This works since there are at max 2 people per boat

O(nlogn) time. This is to sort and O(n) time to run 2 pointer solution
O(n) space to sort
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        l = 0
        r = len(people)-1

        res = 0
        while l<=r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                res += 1
            else:
                r -= 1
                res += 1
        
        return res
        