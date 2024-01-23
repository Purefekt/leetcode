"""
O(1) push and O(n) pop/top using 2 queues.
Create 2 queues, and append to whichever is not empty.
For pop, transfer n-1 elements from the filled queue to the empty queue.
Then return the remaining element.
For top, do the same but also push the remaining element to the the other queue.

O(1) time for push, O(n) time for pop/top.
O(n) space for the 2 queus.
"""

class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)
        

    def pop(self) -> int:
        # transfer n-1 to the other queue and return the left over
        if self.q1:
            n = len(self.q1)
            for i in range(n-1):
                popped = self.q1.pop(0)
                self.q2.append(popped)
            res = self.q1.pop(0)
            return res
        else:
            n = len(self.q2)
            for i in range(n-1):
                popped = self.q2.pop(0)
                self.q1.append(popped)
            res = self.q2.pop(0)
            return res
        

    def top(self) -> int:
        # transfer n-1 to the other queue. Store left over in result and then also transfer it to the other queue
        if self.q1:
            n = len(self.q1)
            for i in range(n-1):
                popped = self.q1.pop(0)
                self.q2.append(popped)
            res = self.q1.pop(0)
            self.q2.append(res)
            return res
        else:
            n = len(self.q2)
            for i in range(n-1):
                popped = self.q2.pop(0)
                self.q1.append(popped)
            res = self.q2.pop(0)
            self.q1.append(res)
            return res
        

    def empty(self) -> bool:
        if len(self.q1) + len(self.q2) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()