"""
Create a hashmap with each char and index of its last occurance
Start a loop, go over each character.
Track the last occurance of a character in a set. Do this by keeping a var cur_end, at first it will be the last occurance of the first char
Keep iterating and this value will change since before the last occurance of a given char, another char within the same substring can have a later occurance, so use max
If i==cur_end, this means we are at the last occurance of the char with the last occurance in the entire substring, add the len of this substring to res
Also keep a prev_end var and update it to get the substring correctly

O(n) time to go over all elements once to create hashmap and once to create res
O(1) space since the hashmap will have at max 26 keys and constant number of values.
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashmap = {}
        for i,c in enumerate(s):
            hashmap[c] = i
        
        i = 0
        res = []
        cur_end = 0
        prev_end = 0
        for i in range(len(s)):
            cur_end = max(cur_end, hashmap[s[i]])
            if cur_end == i:
                res.append(cur_end-prev_end+1)
                prev_end = cur_end+1
                cur_end = 0

        return res
