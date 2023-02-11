"""
BFS will give us the min distance from start = 0
The visited set will be handled differently, since we can get to a node in 2 days, either from a blue edge or a red egde
Thus the visited set will contain tuples of 2 elements, (node, edgeColor)
We will only add to the queue if the child has an edge color different from the previous edge and if this has not been visited yet ie (child, edgecolor) not in visited
Update the answers array, it will contain all -1s at first, update it only ONCE ie the very first time we find a node ie when answers[i] == -1

O(n+e) time where n is number of nodes and e is number of edges
O(n+e) space to store the adj list
"""

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        # build the adj list with edge color data
        adj = {i:[] for i in range(n)}
        for src, dst in redEdges:
            adj[src].append((dst, 'red'))
        for src, dst in blueEdges:
            adj[src].append((dst, 'blue'))

        
        # initialize the answers array with all -1s
        answers = [-1 for i in range(n)]
        for i in range(n):

            queue = [(0, None, 0)]
            visited = set()
            while queue:
                node, prev_color, dist = queue.pop(0)
                
                # update the answers array only once for each node ie when the val is still -1
                if answers[node] == -1:
                    answers[node] = dist

                for child, edge_color in adj[node]:
                    if edge_color != prev_color and (child, edge_color) not in visited:
                        queue.append((child, edge_color, dist+1))
            
                visited.add((node, prev_color))
        
        return answers
