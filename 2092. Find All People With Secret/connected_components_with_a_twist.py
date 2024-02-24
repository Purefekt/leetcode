"""
At time 0, both 0 and firstperson have the secret.
We can create a adj list to create the graph and run bfs.
The queue will contain [(0,0), (firstPerson, 0)] initially since they both know the secret at time 0.
For each node popped, we only add the children whose meeting time >= the current time.
But this means we wont traverse the nodes which have a meeting before their parent gets the secret but they might get the secret at a later time through a different parent.
For this, we need an array 'earliest' of size n which stores the time at which a node got the secret.
Initially all elements are math.inf, 0 and firstPerson = 0.
Now we will only add a child to the queue if child_time >= cur_time and earliest[child] > child_time.
Add all nodes popped to a set which is the result.

O(m*(m+n)) time where we have m meetings and n people. We run the while loop O(m+n) times and for each we runa. for loop of time m.
O(m+n) space.
"""

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        adj = {i:[] for i in range(n)}
        for src, dst, time in meetings:
            adj[src].append((dst, time))
            adj[dst].append((src, time))
        
        res = set()
        queue = [(0,0), (firstPerson, 0)]
        earliest = [math.inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        while queue:
            node, cur_time = queue.pop(0)
            res.add(node)
            for child, child_time in adj[node]:
                if child_time >= cur_time and earliest[child] > child_time:
                    earliest[child] = child_time
                    queue.append((child, child_time))
        
        return res
