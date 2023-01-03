"""
Get the position and state of all dominoes which are either L or R and add them to a queue (need a queue to process left to right)
Run a while loop till queue exists, the state can either be L or R
If it is L, then we will check if any element exists to its left, if it does and if it is a '.' then we will set it to L and add the index we changed and L to the queue
If it is R, then we need to perform more complex checks. We first check if any cell exists to its right and if it is a '.' If this is true then we check is a cell exist next to that, if this cell is a L, then we dont change the list and we pop from the queue, since this is the L we would process. If that element doesnt exists or if it isnt an L, we set the next index to R and add to the queue

O(n) time. To go through all dominoes which can be L or R. in the worst case this is all of the dominoes
O(n) space to store in queue
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        dom = list(dominoes)

        queue = []
        for i,c in enumerate(dom):
            if c == 'L' or c == 'R': 
                queue.append((i,c))
        
        while queue:
            index, state = queue.pop(0)

            if state == 'L':
                if index > 0 and dom[index-1] == '.':
                    dom[index-1] = 'L'
                    queue.append((index-1, 'L'))
            
            elif state == 'R':
                if index+1 < len(dom) and dom[index+1] == '.':
                    if index+2 < len(dom) and dom[index+2] == 'L':
                        queue.pop(0)
                    else:
                        dom[index+1] = 'R'
                        queue.append((index+1, 'R'))
        
        return ''.join(dom)
