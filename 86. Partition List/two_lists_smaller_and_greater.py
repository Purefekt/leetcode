"""
Create 2 lists, Less than and Greater than (also contains all nodes ==x)
Use dummy pointers for both these new lists and iterate through the original list
If the current node val < x, set the next pointer of the less_than list to this node. Do the same for greater_than list otherwise
After iterating all nodes, set the next pointer of both lists to None
Finally join the less than nodes tail to the next node in greater than list
Return the next element of less than list

O(n) time to iterate all nodes once
O(1) space since we use the original nodes given to us to build the 2 linked lists
""" 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if not head:
            return

        # create a less than and greater than listnodes
        less_than = ListNode()
        greater_than = ListNode()

        # create dummy pointers for both
        d_less = less_than
        d_greater = greater_than


        # iterate through the original list and add them to one of the lists
        while head:
            if head.val < x:
                d_less.next = head
                d_less = d_less.next
            else:
                d_greater.next = head
                d_greater = d_greater.next
            
            head = head.next
        
        # set the next pointers for both lists as None
        d_less.next = None
        d_greater.next = None
        
        # # join the two lists.
        d_less.next = greater_than.next

        return less_than.next
        