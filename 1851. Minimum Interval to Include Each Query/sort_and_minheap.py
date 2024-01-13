"""
Sort the intervals and queries in ascending order.
We will traverse the queries from smallest to largest while also traversing the intervals from the left ones to right ones.
For each query, get all intervals where the interval's start is <= query.
Add this interval's size and end to a minheap --> (size, end). While doing this, pop this interval from the intervals array.
Now remove all intervals from the minheap which end before q, ie check the top element and remove it if the end < q.
Now if the minheap is empty, there doesnt exist any interval which satisfies q, else the top element of the minheap is the answer, add it to res.
Do not remove this from the minheap though since it might also satisfy other q's.
Since the result should be in the order of original queries, we need to maintain the original index of the queries.
For this encode the queries array with (q, index) and then sort it.
Then initialize result = [0] * len(query) and then add the solution of each query to its given index in result.

O(nlogn + qlogq) time where n is the size of intervals and q is the size of queries. nlogn time to sort intervals and qlogq time to sort queries. Then we do at most 1 pass over all queries and pop each interval from intervals at most once and then pop it from the minheap at most once, the minheap addition and popping takes nlogn time as well.
O(n+q) space used by sorting.
"""

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # encode indexes into queries to correctly produce output
        for i,q in enumerate(queries):
            queries[i] = (q, i)
        intervals.sort()
        queries.sort()

        minheap = []
        heapq.heapify(minheap)

        res = [0] * len(queries)

        for q,i in queries:
            # add all intervals which are valid to the minheap
            while intervals and intervals[0][0] <= q:
                start, end = intervals.pop(0)
                size = end - start + 1
                heapq.heappush(minheap, (size, end))
            
            # remove all intervals from minheap which end before q
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            
            # add the minheap's top element's size to the result
            if not minheap:
                res[i] = -1
            else:
                res[i] = minheap[0][0]
        
        return res
