
"""
DP. Dp tree, each node of this dp tree is the max profit when that given node is the root of that subtree.
The value at root node will be the max profit when the subtree is the input tree
Get the level order traversal of the tree.
For the last level, put the nodes in a hashmap and initialize their values to [node.val, 0]
First element is the maxprofit when that node is the root, the second element is the profit sum of its children
Fill the dp array where for profit we take the max of the nodes val and its grandchildren, which is stored as the 2nd element of its children nodes AND the sum of its childrens profit (when we do not rob that node)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # get level order traversal
        level_order = []
        queue = [root]
        while queue:
            curr_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
                curr_level.append(node)
            level_order.append(curr_level)
        
        # dp hashmap. key=node : value=[max profit of subtree with this node as root, profit of its children]
        dp = {}
        # initialize last row to node:[node.val, 0]
        for node in level_order[-1]:
            dp[node] = [node.val, 0]
        
        # fill the nodes bottom up
        for i in range(len(level_order)-2, -1, -1):
            for node in level_order[i]:
                node_left_val = 0
                node_right_val = 0
                node_left_children_val = 0
                node_right_children_val = 0
                
                if node.left:
                    node_left_val = dp[node.left][0]
                    node_left_children_val = dp[node.left][1]
                if node.right:
                    node_right_val = dp[node.right][0]
                    node_right_children_val = dp[node.right][1]
                
                max_profit_at_node = max(node.val+node_left_children_val+node_right_children_val, node_left_val+node_right_val)
                children_profit = node_left_val + node_right_val
                
                dp[node] = [max_profit_at_node, children_profit]
        
        # sol is the val at root node
        return dp[root][0]
                    
                