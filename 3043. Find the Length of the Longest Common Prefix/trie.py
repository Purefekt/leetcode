"""
Trie.
Create a trie with all numbers from arr1. Note that we dont need to account for end of a number since its just prefix matching.
Then iterate through each number in arr2 and see how far we can traverse the trie.
Track the longest depth.

O(m+n) time where m is size of arr1 and n is size of arr2. It takes m*d time to insert all nums in the trie, d being the number of digits, which can be 8 so treat as constant. Search for n nums takes n*d time.
O(m) space used by the trie which takes m*d space.
"""

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        # create trie with arr1 nums
        root = TrieNode()
        for n in arr1:
            num = str(n)
            dummy = root
            for c in num:
                if c not in dummy.children:
                    dummy.children[c] = TrieNode()
                dummy = dummy.children[c]
        
        # see how far we can travel for each num in arr2
        res = 0
        for n in arr2:
            num = str(n)
            cur = 0
            idx = 0
            dummy = root
            while idx < len(num) and num[idx] in dummy.children:
                cur += 1
                dummy = dummy.children[num[idx]]
                idx += 1
            res = max(res, cur)
        
        return res
