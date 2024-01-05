"""
Simple graph problem using bfs to find the shortest path.
What makes it tricky is setting up the adj list.
One way is to run a nested loop on the input and compare both words.
Comparing two words uses m time where m is length of word and for n words, we need to compare n^2 times. thus m*n^2.
Since the constraits are that m<=10 and n<=5000, m<<n. So we can try another way.
For each word, we can get all the patterns it accepts, ie remove one character and replace it with anything.
hit -> *it, h*t, hi*, where * means any character. 
Create an adj list where key is a pattern and the value is the words that make it, this is created in m^2*n time which is faster due to the constraits being this way.
Then run bfs, to get the child of a given word, go through all of its patterns and then use the hashmap to access the children.

O(m^2*n) time to create adj list and run bfs.
O(m^2*n) for adj list, O(m*n) for the queue.
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        adj = collections.defaultdict(list)
        # create a hashmap of patterns to words which satisy it
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)
        
        # run bfs
        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            node, depth = queue.pop(0)
            if node == endWord:
                return depth
            if node in visited:
                continue
            # to get children of node, visit all the children of ALL patterns of this node
            for i in range(len(node)):
                pattern = node[:i] + '*' + node[i+1:]
                for child in adj[pattern]:
                    if child not in visited:
                        queue.append((child, depth+1))
            visited.add(node)
        
        return 0
