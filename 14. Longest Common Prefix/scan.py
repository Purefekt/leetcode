"""
Set the first word as common.
Then iterate from the 2nd till last word and keep making common shorter.

O(s) time where s is the sum of all chars of the string.
O(s) space.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = strs[0]

        for i in range(1, len(strs)):
            p = 0
            while p<len(common) and p<len(strs[i]) and common[p] == strs[i][p]:
                p += 1
            common = common[:p]
        
        return common
