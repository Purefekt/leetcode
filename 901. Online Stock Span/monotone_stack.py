"""
Monotonic decreasing stack.
The spanner will be a monotone stack.
For each price we add 2 things to the stack, (price, span).
When we see a new price, pop all the prices in stack which are smaller than or equal to it, while also summing up the spans of all of them.
Once we hit a price > current price or if the stack is empty, then add 1 to the sum of spans. This is the span of current price.
Then add this to the stack and continue.

O(1) time for next call. This is because if there are total n calls, we can only pop from the stack a total of n times. Thus each next call will take n/n or O(1) time.
O(n) space to store the spanner.
"""

class StockSpanner:

    def __init__(self):
        self.spanner = []

    def next(self, price: int) -> int:

        count = 1
        while self.spanner and price >= self.spanner[-1][0]:
            count += self.spanner[-1][1]
            self.spanner.pop()
        
        self.spanner.append([price, count])
        return count
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)