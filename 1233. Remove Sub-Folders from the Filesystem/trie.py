"""
Create a trie with the folder paths and mark each end as e.
Then build the result using this trie by running dfs.
But always stop a path as soon as we hit the first end, since we do not care of subsequent end ie sub folders.

O(n) time to build the trie and then n time to build the result.
O(n) spcae to store trie.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()

        for paths in folder:
            p = paths.split('/')[1:]
            dummy = root
            for c in p:
                if c not in dummy.children:
                    dummy.children[c] = TrieNode()
                dummy = dummy.children[c]
            dummy.end = True
        
        stack = [(root, [])]
        res = []
        while stack:
            node, path = stack.pop()
            if node.end == True:
                f = '/' + '/'.join(path)
                res.append(f)
                continue
            for child in node.children:
                new_path = path[:]
                new_path.append(child)
                stack.append((node.children[child], new_path))
        
        return res
        