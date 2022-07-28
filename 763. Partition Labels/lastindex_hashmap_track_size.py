"""
create a hashmap, char:lastindex. Each unique character in the string and its last position
Next loop through the string and keep a size counter and max_lastindex variable
on each character, update the max_lastvariable to max of itself and the lastvariable of current char + inc size by 1 on each iteration
when current character index == max_lastindex, this means all characters in this substring are only in this substring. At this point append the current size to the output, and set size to 0 and repeat.
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # build hashmap of lastindex
        lastindex_map = {}
        for i in range(len(s)):
            lastindex_map[s[i]] = i
        
        # all pointers and counters
        size = 0
        max_lastindex = 0
        output = []
        for i in range(len(s)):
            max_lastindex = max(max_lastindex, lastindex_map[s[i]])
            size += 1
            
            if i == max_lastindex:
                output.append(size)
                size = 0
        
        return output
    