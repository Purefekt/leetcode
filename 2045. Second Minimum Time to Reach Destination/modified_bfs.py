"""
This solution doesnt work.
The main part which is getting second min distance works using bfs.
This is done by maintaining 2 visited hashmaps and allowing to add nodes until both have been filled.
But the part with change and time doesnt work and i am too tired to debug.
"""

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        # create adj list
        adj = {i:[] for i in range(1, n+1)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # run bfs and get the first and second earliest times each node is visited
        visited_first = {}
        visited_second = {}
        queue = [(1,0)]

        while queue:
            node, dis = queue.pop(0)
            if node in visited_first and node in visited_second:
                continue
            
            for child in adj[node]:
                queue.append((child, dis+1))
            
            if node not in visited_first:
                visited_first[node] = dis
            else:
                visited_second[node] = dis

        if change == 1:
            return visited_second[n] * time

        res = 0
        for i in range(visited_second[n]):
            if i == visited_second[n]-1:
                return res+time
            
            if res//change == (res+time)//change:
                res += time
            else:
                if (res+time)%change == 0:
                    res += time+change
                else:
                    next_wait = math.ceil((res+time)/change)*change
                    res = max(res+time, next_wait)
