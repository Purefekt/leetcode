"""
If we connect any 2 nodes, the diameter can be 1 of 3.
Either the diameter of graph1.
Or the diameter of graph2.
Or the diameter where edge goes through the newly added edge between the two trees.
First find the diameter of both graphs.
Now we connect the mid node of each diameter to each other.
If we connect the start/end of the diameter of tree1 to the start/end of the diameter of tree2, then we will have the MAX possible diameter.
But if we connect it to the mid node, we will basically cut the diameter in half on each side and thus MINIMIZE the possible diameter.

O(n+m) time. n time to create adj list for tree1 and m time to create it for tree2. get max diameter runs in n/m time for each.
O(n+m) space used by stack for each.
"""

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        # create adj list for both
        adj1 = collections.defaultdict(list)
        for a,b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)
        
        adj2 = collections.defaultdict(list)
        for a,b in edges2:
            adj2[a].append(b)
            adj2[b].append(a)
        
        # dfs to get diameter
        def get_max_diameter(adj):
            visited = {}
            def dfs(node):
                child_heights = []
                heapq.heapify(child_heights)
                visited[node] = 0

                for child in adj[node]:
                    if child in visited:
                        continue
                    this_child_height = dfs(child)
                    heapq.heappush(child_heights, -this_child_height)
                
                max_child_path = -child_heights[0] + 1 if child_heights else 0
                # get the 2 heighest child heights to get the diameter
                diameter = 0
                for _ in range(min(2, len(child_heights))):
                    h = heapq.heappop(child_heights)
                    diameter += (-h + 1)
                
                visited[node] = diameter
                return max_child_path
            
            dfs(0)
            return max(visited.values())
        
        max_d1 = get_max_diameter(adj1)
        max_d2 = get_max_diameter(adj2)

        # we need to connect the mid node of diameter of each graph to create the min diameter
        return max(
            math.ceil(max_d1/2) + math.ceil(max_d2/2) + 1,
            max_d1,
            max_d2
        )
