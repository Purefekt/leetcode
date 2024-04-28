"""
SuperTricky: https://www.youtube.com/watch?v=T81Bpx2OmS4&ab_channel=CheatCodeNinja
We can find it brute force in n^2 time.
Suppose example 1 tree, rooted at 0, we can root it at any node since it is undirected.
If we root at 0, we can find the final solution for 0 which is 8.
Now if we break the edge between 0 and 2, we get 2 subtrees.
The number of nodes in subtree rooted at 2 has 4 nodes. The other subtree has n-4=2 nodes.
The 4 nodes in the subtree rooted at 2 are 1 closer to 2 than to 0.
The 2 nodes in the subtree rooted at 0 are 1 farther to 2 than 0.
So we can take res[0] -> 8 and subtract 4 for the 4 closer nodes and add 2 for the 2 further nodes.
In a similar way we can find the solution for all nodes.
In one pass, assume a directed tree rooted at 0 and get the number of nodes in all subtrees rooted at that node. For example 1 it is [6,1,4,1,1,1].
Also during this, we can calculate the final result for just node 0 which is 8.
Now another pass, using the formula and going from top to bottom, we can use the parent's final answer along with the number of nodes in the subtree at that node to get its res.

O(n) time for 2 passes over all nodes.
O(n) space used by call stack in each pass.
"""

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = collections.defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # get number of nodes in each subtree when rooted at that node
        subtree_nodes = [0] * n
        # also get the final result for node 0
        node_zero_res = 0
        
        def dfs(node, parent, depth):
            # since a subtree at a node will atleast have itself 
            total = 1
            nonlocal node_zero_res
            node_zero_res += depth
            for child in adj[node]:
                if child == parent:
                    continue
                total += dfs(child, node, depth+1)
            subtree_nodes[node] = total
            return total
        
        dfs(0, None, 0)
        ans = [0] * n
        ans[0] = node_zero_res
        
        def dfs2(node, parent):
            for child in adj[node]:
                if child == parent:
                    continue
                # res[child] = result of parent - (number of nodes when child as root of subtree) + (number of nodes which remain)
                ans[child] = ans[node] - subtree_nodes[child] + (n-subtree_nodes[child])
                dfs2(child, node)
        
        dfs2(0, None)
        return ans
                