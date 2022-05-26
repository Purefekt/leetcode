"""
Solve this with a list. Each element in the list is a tuple of 2 elements. First is the value being pushed on the stack and second is the current min value. The getMin value
will be the 2nd element of the last tuple in the main list.
"""

class MinStack:

    def __init__(self):
        # initialize a stack as a list
        self.stack = list()
        

    def push(self, val: int) -> None:
        # if stack is empty, then push a tuple (val,val) to the list
        if not self.stack:
            self.stack.append((val, val))
        # else stack not empty, then push a tuple with val as the first element and min of val and previous min val which is the 2nd element of the last tuple
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        # the top element is the first element of the last tuple in the list
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        # min is the second element of the last tuple in the list
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()