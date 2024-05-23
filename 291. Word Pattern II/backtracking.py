"""
Backtracking.
For each char in pattern, try different strings by starting from size 1 till the max it can.
For this we need to use a hashmap to keep track of the current mapping.
Since mapping is unique both ways, we cannot map the same word to a char, for this keep track of all strings currently used.
Helper function takes p_idx, s_idx, mapping, used.
Base case if p_idx == len(pattern). Return True if s_idx == len(s), else False.
Get the current char and see if it exists in mapping.
If it does not, we need to try all strings which start at s_idx till len(s).
Add mapping, add string to used and try, then backtrack by removing from used and deleting from mapping.
If current char is already in mapping, check if the next part if the same string which is in mapping.

O(s^p) where s is size of s and p is size of p. The depth of tree is size of pattern and branching factor is s.
O(s+p) since call stack is of size s and hashmap takes p.
"""

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        
        def helper(p_idx, s_idx, mapping, used):
            if p_idx == len(pattern):
                if s_idx == len(s):
                    return True
                else:
                    return False
            
            char = pattern[p_idx]
            # try different combos for current char
            if char not in mapping:
                for i in range(s_idx, len(s)):
                    string = s[s_idx:i+1]
                    if string not in used:
                        mapping[char] = string
                        used.add(string)
                        if helper(p_idx+1, i+1, mapping, used) is True:
                            return True
                        used.remove(string)
                        del mapping[char]            
            # if a mapping already exists:
            else:
                string = mapping[char]
                if s_idx + len(string) <= len(s):
                    if s[s_idx:s_idx+len(string)] == string:
                        if helper(p_idx+1, s_idx+len(string), mapping, used) is True:
                            return True
            
            return False
        
        return helper(0, 0, {}, set())
