"""
Get the frequency of each task and put it in a maxheap, we will prioritize more frequent tasks.
Use a cache (queue) to hold the tasks on hold.
Run a loop till we have tasks in either max_heap or cache and simulate each unit of time passed
If the max_heap is empty, we do nothing since this is idle time. Else we take the freq and task and reduce the freq by 1 (since this is a maxheap, we increment it by 1). If this task frequency is not yet 0, we add it to the cache -> (freq, task, time_available). 
The time_available will be current_time+n, this is the time when this task can be added back to the maxheap
On each iter we will check the first element of the cache, if this elements time_available == current time, we will add it back to the maxheap

O(k) where k is the total number of tasks to execute including idle tasks. This is the number of times the while loop runs. The heapify operation takes O(n) time and each pop or push takes O(logn) time but since we can have at most 26 elements in the heap, this is O(1) operation
O(1) space since all data structures used will have at most 26 elements
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
    
        if n==0:
            return len(tasks)

        # create freq map
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        
        # put it in a maxheap
        max_heap = []
        for k,v in freq.items():
            max_heap.append((-v,k))
        heapq.heapify(max_heap)

        time = 0
        cache = []

        while max_heap or cache:

            time += 1
            
            # if max_heap is empty, idle state
            if not max_heap:
                pass
            else:
                freq, task = heapq.heappop(max_heap)
                freq += 1
                if freq < 0:
                    cache.append([freq, task, time+n])
            
            if cache and cache[0][2] == time:
                freq, task, _ = cache.pop(0)
                heapq.heappush(max_heap, (freq, task))

        return time
