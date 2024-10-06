"""
2 pointers.
Tokenize both sentences into arrays.
Set one as small and one as long based on sizes.
First check the same number of words from the left side.
Then check the same number of words from right side (can just reverse the arrays to check same as left).
If left + right >= size of smaller sentence, then we can say that its possible.
s1: A,B,C,D,B,B
s2: A,B,B
Left = 2 and right == 2.
2 + 2 >= 3.

O(n+m) time where n is size of s1 and m is size of s2.
O(n+m) space used by tokenizes strigns.
"""

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')
        
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        # check left side similarity
        left = 0
        while left < len(s1) and left < len(s2) and s1[left] == s2[left]:
            left += 1
        # check right side similarity
        s1_rev = s1[::-1]
        s2_rev = s2[::-1]
        right = 0
        while right < len(s1_rev) and right < len(s2_rev) and s1_rev[right] == s2_rev[right]:
            right += 1
        
        if left+right >= len(s2):
            return True
        return False
        