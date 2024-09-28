"""
Double linked list.
Start with creating 2 nodes, one is head and one is tail.
Set tail.next to head and set head.prev to tail.
The DLL looks like (tail) <=> (head).
Now to add a node at tail, we add it right next to tail and similarly do it for head.
The node next to tail is always last in. 
The node prev to tail is always first in.
Keep a cur size int which shows the current size of the list.
Example list: (tail) <=> (2) <=> (1) <=> (3) <=> (head).
Here if we do delete last, then 2 is removed, if we do delete first, then 3 is removed.

O(1) time for each operation.
O(k) space used by K nodes.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.cur_size = 0
        tail = ListNode(val=-1)
        head = ListNode(val=-1)
        self.last = tail
        self.front = head
        self.last.next = self.front
        self.front.prev = self.last

    def insertFront(self, value: int) -> bool:
        if self.cur_size == self.max_size:
            return False
        
        prev_tmp = self.front.prev
        new_node = ListNode(val=value)
        self.front.prev = new_node
        new_node.next = self.front
        new_node.prev = prev_tmp
        prev_tmp.next = new_node
        self.cur_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.cur_size == self.max_size:
            return False

        nxt_tmp = self.last.next
        new_node = ListNode(val=value)
        self.last.next = new_node
        new_node.prev = self.last
        new_node.next = nxt_tmp
        nxt_tmp.prev = new_node
        self.cur_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.cur_size == 0:
            return False
        
        prev_prev_tmp = self.front.prev.prev
        self.front.prev = self.front.prev.prev
        prev_prev_tmp.next = self.front
        self.cur_size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.cur_size == 0:
            return False

        nxt_nxt_tmp = self.last.next.next
        self.last.next = self.last.next.next
        nxt_nxt_tmp.prev = self.last
        self.cur_size -= 1
        return True

    def getFront(self) -> int:
        if self.cur_size == 0:
            return -1
        return self.front.prev.val

    def getRear(self) -> int:
        if self.cur_size == 0:
            return -1
        return self.last.next.val

    def isEmpty(self) -> bool:
        if self.cur_size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.cur_size == self.max_size:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()