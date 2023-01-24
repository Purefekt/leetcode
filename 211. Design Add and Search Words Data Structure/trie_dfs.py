"""
Trie. Build the trienode in addWord
In search use DFS, we if the char is not a dot, we go down that path, else if it is a dot, we add all the children of that node to the stack
For this stack will contain the Trinode and the index of the word. Start with [(root, 0)]
If index == len(word), we will check if the node is end_node, if True then return True else continue to explore other paths in the stack
If the stack empties without a return True, this means there is no path and return False
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        dummy = self.root

        for c in word:
            if c not in dummy.children:
                dummy.children[c] = TrieNode()
            dummy = dummy.children[c]
        dummy.end_node = True
        

    def search(self, word: str) -> bool:
        dummy = self.root

        stack = [(dummy, 0)]
        while stack:
            node, idx = stack.pop()

            # exit statement
            if idx == len(word):
                if node.end_node is True:
                    return True
            else:
                c = word[idx]

                if c != '.':
                    if c in node.children:
                        stack.append((node.children[c], idx+1))
                else:
                    for child in node.children:
                        stack.append((node.children[child], idx+1))

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)