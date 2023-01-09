"""
First sort the input with the source in mind. Since we will pick up people from left to right only
Run a simulation and keep a track of number of people at anu point in the entire trip, if it ever exceeds the capacity, return False
For each trip, add the number of passengers to num_people. Now we need to see if any people got off at that stop, if they did then subtract those many from num_people
Now we need to check for capacity.
To get the people who might exit at a stop, we can use a minheap with (end, number_people). This will always give us the earliest stopping trip and its count of passengers
For any src, if there is any dst which is at or before it, means people got out.

O(nlogn) time. O(nlogn) to sort and O(logn) to get the min element in the heap, which can be done at most n times thus O(nlogn) for minheap as well
O(n) time to store the heap
"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # sort according to start position
        trips.sort(key = lambda x:x[1])

        # check the num people at every position and see if it exceeds capacity
        pq = []
        heapq.heapify(pq)
        num_people = 0

        for i in range(len(trips)):
            count_people, src, dst = trips[i]
            num_people += count_people
            
            # pop from pq till end time of popped trip is <= start of current trip
            while pq and pq[0][0] <= src:
                _, remove_people = heapq.heappop(pq)
                num_people -= remove_people
            
            # check num_people val
            if num_people > capacity:
                return False
            
            # add to pq (dst, count_people)
            heapq.heappush(pq, (dst, count_people))
        
        return True
