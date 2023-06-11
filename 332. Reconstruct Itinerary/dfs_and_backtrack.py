"""
Build the adj list and sort the values. This will ensure the order.
Start the order list with JFK and start with the node JFK.
Go to the first child of this node, remove the child from the adj list and continue.
If we reach a node which has no children left, but the number of items in our order is != len(tickets)+1,
this means we must backtrack.

O(E^2) time where e is the number of egdes or tickets. This is because it will take O(v+e) for the entire graph but each time we go over e edges for backtracking. Since e will always be equal to or more than v, we consider it to be e^2.
O(e) to keep track of adj list of all edges
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # build the graph
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        
        # sort the values
        for v in adj.values():
            v.sort()
        
        def backtrack(order, node):
            if len(order) == len(tickets)+1:
                return order
            
            if node in adj:
                for i in range(len(adj[node])):
                    child = adj[node].pop(i)
                    order.append(child)

                    res = backtrack(order, child)
                    if res is not False:
                        return res

                    adj[node].insert(i, child)
                    order.pop()
            return False
        
        return backtrack(["JFK"], "JFK")
