"""
Recursion with memoization.
Since there are less workers than bikes, we can try to assign a bike to each worker.
To do this, create a hashmap of worker_index to list of all distances to all bikes.
If there are 2 workers and 4 bikes, then our hashmap will have 2 keys and each key will have a list of 4 numbers.
Use a recursion function which takes the worker index and the bikes available to use.
We can use a bit list which is of size len(bikes) and for each index it is either 0 or 1.
1 means the bike is available to be assinged and 0 means the bike is already used.
For each worker_idx, run through all bikes, assign a bike if bike[i] == 1.
For memoization, we can memoize the (worker_index, biked_available bit list).

O(n*2^m) time since there are n different workers and 2^m total versions of the bikes_avail bit list.
O(n*2^m) space for memo table.
"""

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        # create a hashmap of workers -> [distances to all bikes]
        distances = {i:[] for i in range(len(workers))}
        for i in range(len(workers)):
            x1, y1 = workers[i]
            for b in bikes:
                x2, y2 = b
                distances[i].append(abs(x1-x2) + abs(y1-y2))
        

        memo = {}
        def helper(worker_idx, bikes_avail):
            print(1)
            if (worker_idx, tuple(bikes_avail)) in memo:
                return memo[(worker_idx, tuple(bikes_avail))]

            if worker_idx == len(workers):
                return 0
            
            res = math.inf
            for i in range(len(bikes)):
                if bikes_avail[i] == 1:
                    bikes_avail[i] = 0
                    res = min(res, distances[worker_idx][i] + helper(worker_idx+1, bikes_avail))
                    bikes_avail[i] = 1
            
            memo[(worker_idx, tuple(bikes_avail))] = res
            return res
        
        # mark all bikes as available. 1 means available and 0 means used
        bikes_avail = [1] * len(bikes)

        return helper(0, bikes_avail)
