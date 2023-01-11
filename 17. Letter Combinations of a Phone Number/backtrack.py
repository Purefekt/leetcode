"""
Backtracking
Create a hashmap to map digits to their letter lists
Build a list of all letter lists in order
Backtrack on the options list, at the first level we have the chars from the first list in options
In the second level, we have the chars from the second list in options and so on

O(4^n * n) time. This is because the max number of chars per digit is at 7 and 9 which is 4. 
O(n) space for the size of stack
""" 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return

        hashmap = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        options = []
        for c in digits:
            options.append(hashmap[c])
        
        res = []
        def backtrack(digit_idx, combo):
            if len(combo) == len(digits):
                res.append(''.join(combo.copy()))
                return
            
            for i,c in enumerate(options[digit_idx]):
                combo.append(c)
                backtrack(digit_idx+1, combo)
                combo.pop()
        
        backtrack(0,[])
        return res
