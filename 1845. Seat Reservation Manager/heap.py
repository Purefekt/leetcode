"""
Use Heap.

O(nlogn) time for n number of calls. Each reserve or unreserve operation takes logn times. It can be called n times.
O(n) space to store heap.
"""

class SeatManager:

    def __init__(self, n: int):
        self.pq = [i for i in range(1, n+1)]
        heapq.heapify(self.pq)

    def reserve(self) -> int:
        reserved_seat = heapq.heappop(self.pq)
        return reserved_seat
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.pq, seatNumber)

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)