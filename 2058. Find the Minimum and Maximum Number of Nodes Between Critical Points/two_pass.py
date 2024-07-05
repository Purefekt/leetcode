"""
Two pass.
Get indexes of all critical points.
Get min by comparing adjacent points and getting the min.
Max is just last - first.
Can do in one pass by tracking largest and smallest and also getting min_dis by comparing current and next. Uses constant space.

O(n) time for 2 passes, one over the input list and one over critical points.
O(n) space used by critical points.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        # find indexes of critical points
        cp = []
        i = 0
        dummy = head
        while dummy and dummy.next and dummy.next.next:
            i += 1
            if dummy.val > dummy.next.val < dummy.next.next.val:
                cp.append(i)
            elif dummy.val < dummy.next.val > dummy.next.next.val:
                cp.append(i)
            dummy = dummy.next
        
        if len(cp) < 2:
            return [-1, -1]
        
        min_dis = math.inf
        for i in range(len(cp)-1):
            min_dis = min(min_dis, cp[i+1] - cp[i])
        
        return [min_dis, cp[-1]-cp[0]]
