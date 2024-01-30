"""
Get mappings of all words to their position on the grid.
Set current position to (0,0) and for each char in target, get the diff.
For a diff (x,y), x defines the up or down and y defines left or right.
Positive x means go down, negative x means go up.
Positive y means go right, negative y means go left.
For both kinds, simpy add the distance * the letter where we need to go.
NOTE: An edge case is z, we cannot go right from z, since that is out of bounds,
thus always go left first and up first, and only then go right and down.

O(n) time where n is the size of target. 
O(1) space, the pos hashmap takes constanct space. 
"""

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        pos = {}
        count = 0
        for i in range(5):
            for j in range(5):
                pos[chr(ord('a') + count)] = [i,j]
                count += 1
        pos['z'] = [5,0]

        cur_pos = [0,0]
        res = ''

        for c in target:

            diff = tuple(map(lambda x,y: x-y, pos[c], cur_pos))
            cur_pos = pos[c]
            
            if diff[1] < 0:
                res += 'L' * abs(diff[1])
            if diff[0] < 0:
                res += 'U' * abs(diff[0])
            if diff[1] > 0:
                res += 'R' * abs(diff[1])
            if diff[0] > 0:
                res += 'D' * abs(diff[0])
            
            res += '!'
        
        return res
