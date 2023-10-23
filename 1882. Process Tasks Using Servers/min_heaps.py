"""
2 min heaps.
Min heap => free_servers => (weight of server, index of server).
Min heap => busy_till => [free after this time, (weight of server, index of server)].
Iterate over the tasks, set time to max(time, i). This will either increment time by 1 or keep it as is if time > i.
If there are no free servers, then advance the time to the earliest server availability using busy_till.
Transition busy servers to free servers if current time >= busy till time.
Now assign the ith server to the smallest free server and add this to res.
And transition this server to busy with the new time when it will be busy till.

O(mlogn) time where m is the length of tasks and n is the number of servers.
O(n+m) time for both heaps
"""

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        res = [0] * len(tasks)

        time = 0

        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        busy_till = []
        heapq.heapify(busy_till)

        for i in range(len(tasks)):
            time = max(time, i) # time can be more than i

            # if there are no free servers, advance time to the earliest server availability
            if not free_servers:
                time = busy_till[0][0]
            
            # transition busy servers to free servers is current time >= busy till time
            while busy_till and busy_till[0][0] <= time:
                _, s = heapq.heappop(busy_till)
                heapq.heappush(free_servers, s)
            
            # now assign ith server to the smallest free server
            task_time = tasks[i]
            smallest_server = heapq.heappop(free_servers)
            # add to res
            res[i] = smallest_server[1]
            # transition server to busy => [time+task_time, smallest_server]. smallest_server is of format (weight, index)
            heapq.heappush(busy_till, [time+task_time, smallest_server])
        
        return res
