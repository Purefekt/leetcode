"""
Merge 2 lists at a time and repeat.
Instead of merging all lists one by one, which takes k-1 time.
Go through the entire list of lists and merge 2 at a time.
Then update lists to be the result of these mergers. If there were 6 lists in lists, then after merging we will have 3.
Repeat this till there is only a single list in lists.
This reduces the number of lists merged to logk.
If we have the list of lists [[1], [2], [3], [4]], we first merge and get [[1,2], [3,4]] and finally [[1,2,3,4]] and return lists[0].

O(nlogk) time. For each merge, we need to go over n nodes, but we only need logk mergers.
O(1) space since we only use pointers.
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

        while len(lists) > 1:

            mergedLists = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = []
                if i+1 < len(lists):
                    list2 = lists[i+1]
                
                resList = mergeTwo(list1, list2)
                mergedLists.append(resList)
            
            lists = mergedLists
        
        return lists[0]
