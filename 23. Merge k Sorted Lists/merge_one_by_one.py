"""
Merge lists one by one.
Suppose there are k lists.
Set the first list in lists as the head and then run a loop k-1 times from 1->k, merging each list into the head.
If we have the lists [[1], [2], [3], [4]], we would merge and get [1,2], [1,2,3] and finally [1,2,3,4]

O(n*k) time. If there are n nodes, we repeat the work k times for k lists.
O(1) space since we use pointers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwo(list1, list2):

            head = ListNode()
            dummy = head
            d1 = list1
            d2 = list2

            while d1 and d2:
                if d1.val < d2.val:
                    dummy.next = d1
                    d1 = d1.next
                else:
                    dummy.next = d2
                    d2 = d2.next
                dummy = dummy.next
            
            if d1:
                dummy.next = d1
            if d2:
                dummy.next = d2
            
            return head.next
        
        if not lists:
            return

        head = lists[0]

        for i in range(1, len(lists)):
            head = mergeTwo(lists[i], head)
        
        return head
