# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        
        odd = 0
        even = 0

        dummy = head
        while dummy:
            even_score = dummy.val
            odd_score = dummy.next.val
            if even_score > odd_score:
                even += 1
            elif odd_score > even_score:
                odd += 1
            dummy = dummy.next.next
        
        if odd > even:
            return "Odd"
        elif even > odd:
            return "Even"
        else:
            return "Tie"
            