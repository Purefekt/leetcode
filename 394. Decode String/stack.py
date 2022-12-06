"""
Use a stack and iterate over all items one by one.
Add numbers as a whole to the stack, add 30 and not 3,0
Add letters one by one
Add '[' as it is
When we hit a ']', pop all elements till we hit a '[' to create a string. Then pop once more and multiply the string those many times.
Put this string, char by char back into the stack in reverse order. When the loop ends, we will have the correct output in the stack as a list of chars.

O(maxK^countK * n). MaxK is the maximum value of k, countK is the count of nested k and n is the max length of an encoded string. For 20[a10[bc]], maxK is 20, countK is 2 since there are 2 nested k values and n is 2 since the max len of an encoded string is 2(bc)

O(sum(maxk^countK * n)) Max stack size would equal to the sum of all decoded strings.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        factor = ''
        for i in range(len(s)):
            if s[i].isnumeric():
                factor += s[i]
            elif s[i] == '[':
                stack.append(int(factor))
                factor = ''
                stack.append('[')
            elif s[i].isalpha():
                stack.append(s[i])
            elif s[i] == ']':
                cur_str = ''
                while stack:
                    token = stack.pop()
                    if token == '[':
                        break
                    cur_str += token
                cur_str *= stack.pop()

                # put this back in the stack in reverse order
                for j in range(len(cur_str)-1, -1, -1):
                    stack.append(cur_str[j])
                
        
        return ''.join(stack)
