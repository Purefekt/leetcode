"""
All methods are simple except min_val. For that everytime we push a new element to the stack, it will be a tuple of two values.
(val, cur_min). Val will be the integer pushed and cur_min will be the min of the val and the prev min

O(1) time
O(n) space to store the stack in a list
"""

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()