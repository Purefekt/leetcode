"""
Simulation.
Create a circle with an array of size n.
Run for n-1 rounds, each time eliminate the correct one.
To act as a circle, use % to wrap around.

O(n) time to remove n-1 people.
O(n) space used by circle array.
"""

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        circle = [i for i in range(1, n+1)]

        idx = 0
        for _ in range(n-1):
            # in each round, get the index to eliminate
            idx += k-1
            idx %= len(circle)
            circle.pop(idx)

        return circle[0]
