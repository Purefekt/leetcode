# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # initialize an empty linked list
        dummy = ListNode()
        # tail pointer will be used to adjust current nodes next
        tail = dummy
        
        # while list1 and list2 are not None, if either is None, loop ends. This means one list has ended, the remaining elements in the other list will all be sorted and greater than all prev elements, so just add that to the current
        while (list1 is not None) and (list2 is not None):
            # if list1 node is larger than list2 node, then point to list2
            if list1.val > list2.val:
                tail.next = list2
                # update list2
                list2 = list2.next
            # else if list1 node is smaller or eq to list2 node, then point to list1
            else:
                tail.next = list1
                # update list1
                list1 = list1.next
            #update tail pointer
            tail = tail.next
        
        # while loop ends when one of the two lists is None. Add the non empty list to the end
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
        
        # dummy list has the first element as 0, so the actual answer is starting from the next node
        return dummy.next
                