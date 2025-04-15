class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # build trie
        root = TrieNode()
        for w in words:
            dummy = root
            dummy.count += 1
            for c in w:
                if c not in dummy.children:
                    dummy.children[c] = TrieNode()
                dummy = dummy.children[c]
                dummy.count += 1
            dummy.end = True
        
        # function to reduce counters from trienodes
        def kill_path(word):
            print(word)
            dummy = root
            dummy.count -= 1
            for c in word:
                dummy = dummy.children[c]
                dummy.count -= 1
        
        m,n = len(board), len(board[0])
        # run dfs from each position, prune when we dont need to search further.
        visit = set()
        res = []
        def dfs(r,c, dummy, word):
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                (r,c) in visit or
                board[r][c] not in dummy.children or
                dummy.children[board[r][c]].count < 1
            ):
                return

            visit.add((r,c))
            word += board[r][c]
            dummy = dummy.children[board[r][c]]
            if dummy.end is True:
                dummy.end = False
                res.append(word)
                kill_path(word)
            
            dfs(r,c+1, dummy, word)
            dfs(r+1,c, dummy, word)
            dfs(r,c-1, dummy, word)
            dfs(r-1,c, dummy, word)
            visit.remove((r,c))
        
        for i in range(m):
            for j in range(n):
                dfs(i,j,root,"")
        
        return res
            