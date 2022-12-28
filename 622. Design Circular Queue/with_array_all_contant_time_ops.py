"""
Solve with Array. Initialize the queue with an array of None's of size k. the head and tail pointer at 0 and the length stored (which is k) and a counter to hold number of elements in the queue.
Enqueue: if the tail pointer cell is None, then we can add a new element. After adding, increment the tail pointer by 1 and its new position will be itself%k since we need to be within the queue
Dequeue: if the head pointer cell is not None, then set this element to None. Increment the head pointer by 1 and its new position will be itself%k since we need to be within the queue
Front: Simply reurn the element at the head pointer. If this element is None, return -1
Rear: Return the element at index tail-1. If the tail is at index 0, then return the last element which is len_queue - 1. If the element is None, return -1
For successful enqueue operations, increment counter by 1 and for successful dequeue operations, decrement counter by 1
isEmpty: if the counter value is 0, return true else false
isFull: if the counter value == len_queue, return true else false

O(1) time. All operations run in constant time
O(k) space, to create an array of size k
"""

class MyCircularQueue:

    def __init__(self, k: int):
        # create an array of fixed size k
        self.circular_queue = [None] * k
        self.head = 0
        self.tail = 0
        self.len_queue = k
        self.count = 0
        

    def enQueue(self, value: int) -> bool:
        if self.circular_queue[self.tail] is None:
            self.circular_queue[self.tail] = value

            self.tail += 1
            self.tail %= self.len_queue

            self.count += 1
            
            return True

        else:
            return False 
        

    def deQueue(self) -> bool:

        if self.circular_queue[self.head] is None:
            return False
        
        else:
            self.circular_queue[self.head] = None
            
            self.head += 1
            self.head %= self.len_queue

            self.count -= 1

            return True


    def Front(self) -> int:
        if self.circular_queue[self.head] is None:
            return -1
        
        return self.circular_queue[self.head]
        

    def Rear(self) -> int:
        if self.tail == 0:
            if self.circular_queue[self.len_queue-1] is None:
                return -1
            else:
                return self.circular_queue[self.len_queue-1]
        else:
            if self.circular_queue[self.tail-1] is None:
                return -1
            else:
                return self.circular_queue[self.tail-1]


    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.count == self.len_queue:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()