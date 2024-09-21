"""
Trie.
Create a trie with the string versions of numbers.
Once the trie is made, traverse it in a dfs manner but also go from the last node to 0th.
So we loop from 9 till 0, this way the path will be correct.

O(n) time.
O(n) space.
""" 

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        root = TrieNode()
        for i in range(1, n+1):
            num = str(i)
            dummy = root
            for c in num:
                if c not in dummy.children:
                    dummy.children[c] = TrieNode()
                dummy = dummy.children[c]
        
        res = []
        stack = [(root, [])]
        while stack:
            node, path = stack.pop()
            if path:
                res.append(int(''.join(path)))
            for i in range(9, -1, -1):
                num = str(i)
                if num in node.children:
                    new_path = path[:]
                    new_path.append(num)
                    stack.append((node.children[num], new_path))
        
        return res
        