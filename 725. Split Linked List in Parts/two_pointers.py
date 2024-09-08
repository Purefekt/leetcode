"""
Two pointers.
Get the size of list and store it as n.
For equal distribution and with the condition that earlier parts have higher size than later parts, we can get it by ceil(n/k).
If n = 10, k = 3, we get ceil(10/3) = 4 and put 4 in first part.
Next we have n=6 and k=2 and repeat.
Use two pointers to maintain start of a segment and end of it.

O(n) time for one pass over the list.
O(1) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        n = 0
        dummy = head
        while dummy:
            n += 1
            dummy = dummy.next
        
        p1 = head
        p2 = head
        res = []
        while k>0:
            size_of_part = math.ceil(n/k)
            for _ in range(size_of_part):
                p2 = p2.next
            res.append(p1)
            # move p1 to just before p2
            while p1 and p1.next != p2:
                p1 = p1.next
            if p1:
                p1.next = None
            p1 = p2
            n -= size_of_part
            k -= 1
        
        return res
