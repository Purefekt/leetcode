"""
Iteration
Make a false head. Use a pointer tail to iterate over and build the new linked list.
Check each node of list1 and list2. point to whichever is smaller.
Once the while loop terminates, one of the two lists are empty, point the end of the tail to the other list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # start with dummy node
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            # if list1 node is smaller, point to it. update tail and list1
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            # else if list2 node is smaller or equal, point to it. update tail and list2
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        
        # add the list which isnt null yet
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next
    