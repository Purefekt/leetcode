"""
Implement a trie like a tree using a class TreeNode which contains a hashmap of its children and a boolean flag to indicate end of a word
To insert, iterate over the word and add to the tree, if a char exists in the tree at that position, continue that path
Search and startwith work in the same way except we check the end_node flag in search

O(m) time where m is the length of the key
O(1) space since at each level we will have at most 26 nodes for all lowercase english chars
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        dummy = self.root

        for c in word:
            if c not in dummy.children:
                dummy.children[c] = TrieNode()
                dummy = dummy.children[c]
            else:
                dummy = dummy.children[c]
        # mark the last node as the end of the word
        dummy.end_node = True
        

    def search(self, word: str) -> bool:
        # go to the end of the word and see if it is the end_node
        dummy = self.root
        
        for c in word:
            if c not in dummy.children:
                return False
            dummy = dummy.children[c]
        
        if dummy.end_node is False:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        # go to the end of the prefix
        dummy = self.root

        for c in prefix:
            if c not in dummy.children:
                return False
            dummy = dummy.children[c]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)