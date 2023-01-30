"""
Create an array of valid options to use which is [1-9]
Use backtracking to add a number to the combination, and update the sum
To not reuse an element, increment the start index to the next in the next recursive call

O(9ck * k) time. 9choosek time since in the worst case we will explore all 9ck possibilities. Each time we get to a base case we copy the array of size k in O(k) time. 
O(k) space for the intermediate combination array and the implicit stack
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        options = [1,2,3,4,5,6,7,8,9]

        res = []
        def backtrack(combo, summ, idx):
            if len(combo) == k:
                if summ == n:
                    res.append(combo.copy())
                return
            
            for i in range(idx, len(options)):
                # small optimization to avoid going further if summ < n since the options are sorted in ascending order
                if summ < n:
                    combo.append(options[i])
                    summ += options[i]
                    backtrack(combo, summ, i+1)
                    summ -= options[i]
                    combo.pop()
        
        backtrack([], 0, 0)
        return res
