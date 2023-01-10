"""
Get the distance from origin to each point and store the (distance, point) into an array
Convert this array to a minheap, the point closest will always be at the top since distance is the key
Pop k times and add to the res.
NOTE: Do not build minheap one by one, since that will take O(nlogn) time since each heappush operation is logn. Build the array in O(n) time and heapify it in O(n) time

O(klogn) time. Each heappop takes O(logn) time and we do this k times
O(n) space to store the heap
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # calculate the distance from origin for each point and put it in a minheap
        minheap = []

        def distance(point):
            x,y = point
            return x**2 + y**2
        
        for point in points:
            minheap.append((distance(point), point))

        # convert to minheap in O(n)
        heapq.heapify(minheap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        
        return res
        