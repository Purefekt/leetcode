"""
2d dp.
First get the freq of all chars at each index.
For ["acca","bbbb","caca"], we get the following.
0 -> {a:1, b:1, c:1}
1 -> {a:1, b:1, c:1}
2 -> {a:0, b:1, c:2}
3 -> {a:2, b:1, c:0} + other chars till z.
Dp func will take the current index of target and the current index of words.
At each index, we can either use it or skip it.
If we skip it, simply increment k since i doesnt change.
If we use it, we need to find how many branches we have ie the frequency of that char at that position among all words.

O(w*k + i*k) time where w is size of words, k is size of each word and i is size of target. w*k time to build the freq hashmap and then i*k time for dp.
O(w*k + i*k) space sice w*k space used by freq hashmap and i*k space used by memo table.
"""

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        mod = 10**9 + 7

        # get freq of all chars a-z at each index
        freq = {}
        for i in range(len(words[0])):
            freq[i] = {j:0 for j in range(26)}
        
        for i in range(len(words)):
            for j in range(len(words[i])):
                char = ord(words[i][j]) - ord('a')
                freq[j][char] += 1

        memo = {}
        def helper(i, k):
            if (i,k) in memo:
                return memo[(i,k)]
            if i == len(target):
                return 1
            if k == len(words[0]):
                return 0
            
            res = 0
            # skip this position
            res += helper(i, k+1)

            # use this position if we can
            target_char = target[i]
            count = freq[k][ord(target_char) - ord('a')]
            res += (count * helper(i+1, k+1))

            memo[(i,k)] = res
            return memo[(i,k)]
        
        return helper(0, 0) % mod
