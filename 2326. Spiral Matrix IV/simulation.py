"""
Simulation.
Use hashmap for direction change.
Go through the result matrix in spiral fashion.
If we hit a wall or a pre visited cell, change direction.

O(m*n) time.
O(m*n) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        res = []
        for i in range(m):
            res_row = [-1 for j in range(n)]
            res.append(res_row)
        
        dummy = head
        dir_change = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1)
        }
        direction = (0,1)
        cur = (0,0)
        visited = set()

        while dummy:
            r,c = cur
            res[r][c] = dummy.val
            next_cell = tuple(map(lambda x,y:x+y, cur, direction))
            i,j = next_cell
            if i>=m or i<0 or j>=n or j<0 or next_cell in visited:
                direction = dir_change[direction]
                next_cell = tuple(map(lambda x,y: x+y, cur, direction))

            visited.add(cur)
            dummy = dummy.next
            cur = next_cell
        
        return res