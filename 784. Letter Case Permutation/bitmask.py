"""
Using Bitmask. For a letter, it can be uppercase or lowercase, 0 or 1
If we have string 'ab' then that can be read as 00. The permutations are 'aB', 'Ab' and 'AB' which are 01, 10, 11.
This can be done by starting from 0 and going till the max value given by number of characters in binary.
In this ex start is 0 and number of chars is 2. Max number rep by 2 bits is 3. So we have 4 permutations for 0,1,2,3

O(2^n *n) In the worst case we have all letters, all of which have 2^n states.
O(2^n *n) space to store binary representations
"""

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        s_list = [c for c in s]

        # find number of letters in s and place their index in a list
        c_idx_list = []
        for i,c in enumerate(s):
            if c.isalpha():
                c_idx_list.append(i)
        
        num_letters = len(c_idx_list)
        start = 0
        end = 0
        for i in range(num_letters):
            end += 2**i
        
        binary_states = []
        # get all permutations of 0 or 1 states of all letters
        for i in range(start, end+1):
            binary_c = bin(i)
            binary_c = binary_c.split('b')[1]
            binary_c_list = []
            for j in range(len(binary_c)):
                binary_c_list.append(binary_c[j])
            if len(binary_c_list)<num_letters:
                for k in range(num_letters - len(binary_c_list)):
                    binary_c_list.insert(0,'0')
            binary_states.append(binary_c_list)
        

        res = []
        for i in range(len(binary_states)):
            for j in range(num_letters):
                if binary_states[i][j] == '0':
                    s_list[c_idx_list[j]] = s_list[c_idx_list[j]].lower()
                else:
                    s_list[c_idx_list[j]] = s_list[c_idx_list[j]].upper()
            res.append(''.join(s_list))


        return res
        