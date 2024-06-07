"""
TRIE.
Create a trie with all words in the dictionary.
For each word in sentence, get the root using the trie by travelling the trie.
Use helper function for this.

O(d*w + s*w) time where d is the size of dictionary, s is the size of sentence and w is the average length of a word. We use d*w time to create the trie and s*w time to find root of each word in sentence.
O(d*w + s*w) space, trie uses d*w space and root words are stores using s*w space.
"""

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode(0)
        for w in dictionary:
            dummy = root
            for c in w:
                if c not in dummy.children:
                    dummy.children[c] = TrieNode(c)
                dummy = dummy.children[c]
            dummy.end = True
        
        def get_root(word):
            dummy = root
            res = ''
            for c in word:
                if dummy.end == True:
                    return res
                if c not in dummy.children:
                    return word
                else:
                    res += c
                    dummy = dummy.children[c]
            return word

        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            sentence[i] = get_root(sentence[i])
        
        return ' '.join(sentence)
