"""
if string has even chars, replace the first non 'a' char with 'a' till the entire length of the string
if string has odd chars, replace the first non 'a' char with 'a' for all chars except the mid char (since changing that would result in a palindrome)

in the edge case where all chars are a, change the last char to b
"""

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        # edge case where len(string) == 1. output will HAVE to be a palindrome, thus output nothing
        if len(palindrome) < 2:
            return ''
        
        # make a list of string
        p_list = []
        for c in palindrome:
            p_list.append(c)
        
        # if even
        if len(p_list) % 2 == 0:
            for i in range(len(p_list)):
                if p_list[i] != 'a':
                    p_list[i] = 'a'
                    return ''.join(p_list)
        
        # if odd
        if len(p_list) % 2 == 1:
            for i in range(0,len(p_list)//2):
                if p_list[i] != 'a':
                    p_list[i] = 'a'
                    return ''.join(p_list)
            for i in range(len(p_list)//2+1, len(p_list)):
                if p_list[i] != 'a':
                    p_list[i] = 'a'
                    return ''.join(p_list)
        
        # if no return still, this means edge case with all a's, set last a to b
        p_list[-1] = 'b'
        return ''.join(p_list)
    