"""
Use Trie
Create a Trie with children hashmap and count
Build the trie by reversing all domains, at each new node, add that domain's count to the node
Now run dfs from the root of the trie, we need all paths  and their count will be the count of the last node in the path's count

O(n) time to go over all domains once
O(n) space to store Trie
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        root = TrieNode()

        for domain in cpdomains:
            count, domain = domain.split(' ')
            domain = domain.split('.')
            domain = domain[::-1]

            dummy = root
            for dom in domain:
                if dom not in dummy.children:
                    dummy.children[dom] = TrieNode()

                dummy.children[dom].count += int(count)
                dummy = dummy.children[dom]
        
        # do dfs and get all paths in TRIE
        stack = [(root, [])]
        res = []
        while stack:
            node, path = stack.pop()
            count = node.count

            if count != 0:
                res.append(str(count) + ' ' + '.'.join(path[::-1]))

            for child in node.children:
                new_path = path.copy()
                new_path.append(child)
                stack.append((node.children[child], new_path))
        
        return res
