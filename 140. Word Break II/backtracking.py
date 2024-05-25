"""
Backtracking.
Try to build sentences for each size of word from a start index of s.
Only continue if that word exists in word_dict.

O(2^n) time since the height is n and branching factor is 2 to either keep or not keep.
O(n) space used by stack and worddict set.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_dict = set(wordDict)

        res = []
        
        def helper(start, combo):
            if start == len(s):
                res.append(' '.join(combo.copy()))
                return
            
            for i in range(start, len(s)):
                word = s[start: i+1]
                if word in word_dict:
                    combo.append(word)
                    helper(i+1, combo)
                    # backtrack
                    combo.pop()
        
        helper(0, [])
        return res
