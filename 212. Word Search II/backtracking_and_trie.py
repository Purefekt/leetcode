"""
Create a Trie containing all the words in words.
For each node in the trie, while adding a character, incremenet the refs counter by 1. This will be used for pruning later.
Run backtracking from each cell in the board and also traverse the trie at the same time. If at any cell, the node.isWord is True, this means we have found a word and add it to res.
We need to prune this path of the trienode so that we dont traverse it again if it is dead. We do this by decrementing the refs counter for all nodes over the path of the word just added to res.
The backtracking recursive function will check if the cell is in bounds, if the current cell exists in node.children, if it is not been visited AND if the refs counter > 0.
Suppose we have a trie a->b->c, and we found the word abc, now it makes no sense to visited a->b->c again so we can prune this branch. But if suppose we had a trie formed with words abc and abd, we can prune c but not ab, since there exists another valid word on this path.

O(m*n*4*(3^l-1)) where m*n is number of cells and l is the maximum length of words. For the backtracking step, suppose the length of word is l. For the very first step, we have 4 possible directions. After that we have 3 possible directions since we cannot go to visited cells, thus we have 3^(l-1) steps for the remaining cells and 4 for the first. And we repeat this for all cells which are m*n.
O(n) space for the trie where n is total number of letters in all words.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r not in range(ROWS) 
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
