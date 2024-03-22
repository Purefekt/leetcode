# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # get size
        n = 0
        dummy = head
        while dummy:
            n += 1
            dummy = dummy.next
        
        half = math.ceil(n/2)

        # reverse the 2nd half
        dummy = head
        for _ in range(half):
            dummy = dummy.next
        
        prev = None
        while dummy:
            nxt_tmp = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = nxt_tmp
        
        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
        