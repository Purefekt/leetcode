"""
Brute Force. 2^n TLE
Go through the entire decision tree and check the final combo at all leafs
To check validity, use a func: check if the combination is valid. There must be equal left and right brackets. Left var increases when we see an open bracket and decreases when we see a closed bracket. If at any point it becomes negative, this means this combo will never be valid. At the end left must be 0 for balance
Recursive func: this function will recursively build the decision tree. Base case is if the combo len is 2n, we will check its validity and add it to the res accordingly. Add open and closed and run recursively.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def check_valid(combo):
            left = 0
            for c in combo:
                if left<0:
                    return False
                if c == '(':
                    left += 1
                else:
                    left -= 1
            if left != 0:
                return False
            return True
        
        res = []
        def generate(combo):
            if len(combo) == 2*n:
                if check_valid(combo) is True:
                    res.append(''.join(combo))
                return
            
            combo.append('(')
            generate(combo)
            combo.pop()
            combo.append(')')
            generate(combo)
            combo.pop()
        
        generate([])
        return res
        