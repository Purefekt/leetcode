"""
Trie.
Create a trie with all words.
Use a new variable count to track the number of times a char appears.
Go through all words again and sum the count while traversing a word.

O(n*m) time where n is size of words and m is average length of word. To create the trie and to traverse it, it takes n*m time.
O(n*m) space used by trie.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()

        for w in words:
            dummy = root
            for c in w:
                if c not in dummy.children:
                    dummy.children[c] = TrieNode()
                dummy = dummy.children[c]
                dummy.count += 1
        
        # traverse all words again to get total sum
        res = []
        for w in words:
            dummy = root
            count = 0
            for c in w:
                if c not in dummy.children:
                    break
                dummy = dummy.children[c]
                count += dummy.count
            res.append(count)
        
        return res
        