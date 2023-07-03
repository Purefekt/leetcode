"""
Create a new head and use pointers at list1 and list2.
Go through the lists and add the smaller and move on.
At the end check if either of the lists remain, then add it to the new list.

O(m+n) time to go through all nodes in both lists.
O(1) space since we just use pointers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        dummy = head
        d1 = list1
        d2 = list2

        while d1 and d2:
            if d1.val < d2.val:
                dummy.next = d1
                d1 = d1.next
            else:
                dummy.next= d2
                d2 = d2.next
            
            dummy = dummy.next
        
        if d1:
            dummy.next = d1
        if d2:
            dummy.next = d2

        return head.next
        