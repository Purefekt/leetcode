"""
Floyd's cycle algorithm. This algorithm tells us the start of a cycle in a linked list.
In the given problem, the start of cycle will be at the duplicate number.
Suppose there are linked list nodes, the node is the index in the array and the element in the array at an index is the next pointer to it.
So for [1,3,4,2,2], node1 -> node3. This is because node1 has element 3 which means it points to the node3. Similarly node3 -> node2 since at nums[3] we have 2.
If we draw this linked list, we notice that the duplicate number is the start of the cycle and node0 will never be a part of the cycle since the nodes point to [1,n] only.
ALGO:
set slow and fast pointers to 0. Move slow once and move fast twice per iteration. Continue till slow==fast.
Once slow==fast, use another slow2 pointer starting at 0. Move both slow and slow2 once per iteration.
When slow == slow2, this is the duplicate.

O(n) time.
O(1) space.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow==fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow==slow2:
                break
        
        return slow
