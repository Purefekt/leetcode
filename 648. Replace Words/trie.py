"""
Create a Trie using all the words in the dictionary. Other than children hashmap and end_node boolean, use another attribute 'word'.
The word will be the final word when the end_node is True. For all intermediate nodes, it will be an empty string
Use a helper function replace word, this will go through all the chars in the word and see if they exist in a trie. At any point when the end_node is true (and we have no exit the function due to a char not being in the children), we will exit with the given word.
Do this for all words in the sentence and return

O(n * avg(l)) time where n is the number of words in dictionary and average l is the average length
O(k) space to store the sentence intermediate list, where k is the number of words in the sentence. The Trie needs O(1) space to store
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False
        self.word = ''

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        root = TrieNode()

        # fill the trie with dictionary words
        for word in dictionary:
            dummy = root
            for c in word:
                if c not in dummy.children:
                    dummy.children[c] = TrieNode()
                    dummy = dummy.children[c]
                else:
                    dummy = dummy.children[c]
            dummy.end_node = True
            dummy.word = word
        
        def replace_word(word):
            dummy = root
            for c in word:
                if c not in dummy.children:
                    return False
                else:
                    dummy = dummy.children[c]
                
                if dummy.end_node is True:
                    return dummy.word
                
            if dummy.end_node is False:
                return False
            return dummy.word
        

        sentence = sentence.split(' ')
        for i,word in enumerate(sentence):
            replaced_word = replace_word(word)

            if replaced_word:
                sentence[i] = replaced_word
        
        return ' '.join(sentence)
