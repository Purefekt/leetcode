"""
Array.
Simply perform the functions as requested.

O(1) for push and pop and O(k) for increment.
O(maxSize) for the stack size.
"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.cur_size = 0
        self.stack = []

    def push(self, x: int) -> None:
        if self.cur_size == self.max_size:
            return
        self.stack.append(x)
        self.cur_size += 1

    def pop(self) -> int:
        if self.cur_size == 0:
            return -1

        res = self.stack.pop()
        self.cur_size -= 1
        return res

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.cur_size)):
            self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)