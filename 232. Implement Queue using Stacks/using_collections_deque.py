class MyQueue:

    def __init__(self):
        # initialize two stacks
        self.stack_1 = collections.deque()
        self.stack_2 = collections.deque()

    def push(self, x: int) -> None:
        # fill all elements in stack_1 as normal
        self.stack_1.append(x)
        

    def pop(self) -> int:
        # remove element from stack_1 and push onto stack_2, repeat this len(stack_1)-1 times. After this stack_1 will have 1 element which will be the the pop element if it were a queue.
        # Then pop from stack_2 and push to stack_1, repeat this till stack_2 is none to go back to original state.
        for i in range(len(self.stack_1)-1):
            curr_element = self.stack_1.pop()
            self.stack_2.append(curr_element)
        
        output = self.stack_1.pop()
        
        # back to original state
        while self.stack_2:
            curr_element = self.stack_2.pop()
            self.stack_1.append(curr_element)
        
        return output
            
        

    def peek(self) -> int:
        return self.stack_1[0]

    def empty(self) -> bool:
        if self.stack_1:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()