"""
Sort the tickets and build an adjacency list. This will give us a sorted adjacency list
Run dfs recursively, if the length of result is the len of tickets + 1, then return True
iterate through the given node's children, for each child, remove it from the adj list and add it to result.
Now run dfs recursively on the child, if its False, then backtrack. Remove this node from the res and add it back int he same pos to the adj list

O(E^2) time where e is the number of egdes or tickets. This is because it will take O(v+e) for the entire graph but each time we go over e edges for backtracking. Since e will always be equal to or more than v, we consider it to be e^2.
O(e) to keep track of adj list of all edges
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()

        adj = {}
        for source, destination in tickets:
            if source not in adj:
                adj[source] = [destination]
            else:
                adj[source].append(destination)
        
        res = ['JFK']
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i in range(len(temp)):
                dest = adj[src].pop(i)
                res.append(dest)
                if dfs(dest) is True:
                    return True
                else:
                    res.pop()
                    adj[src].insert(i,dest)
            return False
        
        dfs('JFK')
        return res
