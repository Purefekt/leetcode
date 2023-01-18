"""
Use Trie. Create a TrieNode class containing a hashmap of children and that node's val
To insert, add the characters one by one as TrieNodes, for the last node add the val (like we add a bool to indicate end of a word)
To sum, use a dummy pointer and go to the end of the prefix, from here use bfs and explore all its children nodes and get the sum of all nodes
Also while checking prefix, first check if it even exists in the trie, if not then return 0

O(k) time for insert. O(k^26) time for sum. Where k is the length of the key.
O(n) space. Linear wrt to input
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        dummy = self.root

        for c in key:
            if c not in dummy.children:
                dummy.children[c] = TrieNode()
                dummy = dummy.children[c]
            else:
                dummy = dummy.children[c]
        dummy.val = val
        

    def sum(self, prefix: str) -> int:

        # get to the end of the prefix
        dummy = self.root
        for c in prefix:
            if c not in dummy.children:
                return 0
            dummy = dummy.children[c]
        
        # run bfs from this to all its children
        summ = 0
        queue = [dummy]
        while queue:
            node = queue.pop(0)
            summ += node.val
            for child in node.children:
                queue.append(node.children[child])
        
        return summ


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)