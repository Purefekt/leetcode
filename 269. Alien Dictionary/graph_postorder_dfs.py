"""
We need to create an adj list where a directed edge is between a lexicographically smaller character to a larger one.
To do this, we can compare all pairs of adjacent words in the list and compare character wise.
For 2 words being compared, the first character they differ on will have an edge from first word's char -> second word's char.
NOTE: if we find any pair incorrectly sorted for example [abc, ab] since it should be [ab, abc], return "".
After creating the hashmap, we can traverse the graph and get the output.
Traversing graph can be done with dfs and getting the postorder result, this is the path in a reversed order.
We can start from any node and run dfs for all nodes.
We also need to check for cycles, to do this we can use a visited hashmap, where visited[node] = True, means this node is in the current path.
Visited[node] = False, means this node has been visited but it is not in the current path.
Return out of the recursive call if we find a child which is visited[child] = True, since this is a cycle.
Think of how to write this recursive function with the example:
{a -> [b], b -> [c], c -> [a]} This has a cycle.
{a -> [b,c], b -> [c], c -> []} This doesnt have a cycle.

O(c) time where c is the length of all words combined.
O(1) space where u is the total number of unique letters since u is 26.
"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # add all unique words as nodes to the adj list
        adj = {}
        for w in words:
            for c in w:
                adj[c] = []

        # create edges between characters using adjacent pairs of words
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]

            # check if they are sorted incorrectly, [abc, ab] is wrong sorting.
            shorter_len = min(len(first), len(second))
            if first[:shorter_len] == second[:shorter_len] and len(first) > len(second):
                return ""

            c = 0
            while c<len(first) and c<len(second):
                if first[c] != second[c]:
                    adj[first[c]].append(second[c])
                    break
                c += 1
        
        # run dfs and create postorder result. Detect cycle if the child is in the current path
        # use a visited hashmap, node -> True means that node is in the path, node -> False means that node is visited but not in current path
        res = []
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            visited[node] = True
            for child in adj[node]:
                if dfs(child) is True:
                    return True
            visited[node] = False
            res.append(node)

            return False
        
        for k in adj:
            if dfs(k) is True:
                return ""
        
        # build output in reverse
        res.reverse()
        return ''.join(res)
