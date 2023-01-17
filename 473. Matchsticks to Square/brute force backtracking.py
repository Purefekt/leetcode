"""
Brute force backtracking
First we check if the sum of matchsticks len is a multiple of 4, if not then return False
Now we need each side to be of length perimeter//4. We will set all sides to 0 and try all combinations on it
Recursive func will take the ith matchstick, if cross the last matchstick, i==len(matchticks) without failing, we have created a valid pairing and return True
We run it for all 4 sides and at each step check if the side + current matchstick is <=side length
To optimize, we can sort the length in a reverse order, since if we have the combo (3,2,1,1), the perimeter is 8 and each side will be 2, but the largest matchstick is 3, thus we will fail at the very first step

O(4^n) time. The height of the tree is n and we have 4 decisions on each level
O(n) space for implicit stack
"""

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        perimeter = sum(matchsticks)
        side_len = perimeter//4

        if side_len*4 != perimeter:
            return False
        
        matchsticks.sort(reverse=True)
        
        sides = [0,0,0,0]
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= side_len:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1) is True:
                        return True
                    sides[j] -= matchsticks[i]
            
            return False
        
        return backtrack(0)
            