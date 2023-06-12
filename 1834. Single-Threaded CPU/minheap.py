"""
Encode the tasks with their indexes since we need to return those. Then sort them.
Set global time to 1 and iterate through the sorted tasks.
Get all the tasks which are available, i.e. get all tasks whose enq time is <= global time.
If there are no tasks whose enq time <= global time, then fast forward time to the next earliest time.
Process the available time with the shortest process time. This is done by using the available queue as a minheap.
For each process we store (processTime, index) in the heap, and this gives us the smallest processing available job.
As we pick a process, update the result with the index

O(nlogn) time. Adding indexes takes O(n) time and then sorting it takes O(nlogn). pushing and popping from heap takes O(nlogn) for n items.
O(n) space to store the tasks list with indexes. The minheap also takes O(n) space.
"""

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # encode indexes to the tasks and sort
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()

        numTasks = len(tasks)
        res = []
        # this minheap contains all tasks available to us
        avail = []
        heapq.heapify(avail)


        time = 1
        while len(res) < numTasks:

            while tasks and time >= tasks[0][0]:
                _, procTime, idx = tasks.pop(0)
                heapq.heappush(avail, (procTime, idx))
            
            # is there is no tasks avail but tasks do remain, then fast forward to the next earliest task
            if not avail:
                time = tasks[0][0]
            
            else:
                procTime, idx = heapq.heappop(avail)
                res.append(idx)
                time += procTime
        
        return res
