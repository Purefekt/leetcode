"""
Get the frequencies.
Then create a result node.
Iterate through all keys and create new nodes with vals.
Attach the nodes and continue.
Return res.next.

O(n) time to create freq hashmap and then another pass to create result.
O(n) space used by frequency map.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        freq = collections.defaultdict(int)
        dummy = head
        while dummy:
            freq[dummy.val] += 1
            dummy = dummy.next
        
        res = ListNode()
        dummy = res
        for k,v in freq.items():
            node = ListNode(v)
            dummy.next = node
            dummy = dummy.next
        
        return res.next
