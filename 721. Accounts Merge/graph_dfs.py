"""
Treat this like a graph problem.
Create an undirected egde between each email in one account.
If we have 2 account with just the emails here [a,b] and [b,c], then a->[b], b->[a,c], c->[b].
This way we can generate connected components. For ease of use a node will be a tuple (email, username).
Use this email at the very end by adding it at the start of a connected component.

O(nk*lognk) time for n number of accounts and k maximum length of an account. In the worst case, all emails belong to a single person. The total number of emails will be n*k which need to be sorted. DFS traversal takes nk operations since an email is traversed at most once.
O(nk) for the stack and visited
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # create an undirected graph where there is an edge between all elements of a user's emails
        # store a node as (email, username) to retain the username info
        adj = {}
        for acc in accounts:
            username = acc[0]
            for i in range(1, len(acc)):
                if (acc[i], username) not in adj:
                    adj[(acc[i], username)] = []
                for j in range(1, len(acc)):
                    if i!=j:
                        adj[(acc[i], username)].append((acc[j], username))
        
        res = []
        # find all connected components in the graph
        visited = set()
        for k,v in adj.items():
            print(k,v)
        for start_node in adj:
            if start_node not in visited:
                # run dfs if its a brand new node:
                username = start_node[1]
                group = []
                stack = [start_node]
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        # add email to the group
                        group.append(node[0])
                        for child in adj[node]:
                            stack.append(child)
                        visited.add(node)
                # sort the group and then add username to the left
                group.sort()
                group.insert(0, username)
                res.append(group)
        
        return res
