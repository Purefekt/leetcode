"""
Backtracking
Recursive function takes the current combo, current sum and index we are at
Base case when summ == target, add this combo to result and return. Or if summ > target, adding more numbers will only increase the summ and never get to target thus return
Loop over the candidates starting at the idx. In each iteration, call backtrack again with the same index since we can reuse numbers

O(n ^ (t/m + 1)) time. The branching factor will be at max all candidates of length n. The height of the tree will be t/m if t is the target and m is the smallest value of the candidates.
O(t/m) space. This will be taken by the intermediate combination arrays and the implicit stack. 
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(combo, summ, idx):
            if summ == target:
                res.append(combo.copy())
                return
            
            if summ > target:
                return

            for i in range(idx, len(candidates)):
                combo.append(candidates[i])
                summ += candidates[i]
                backtrack(combo, summ, i)
                summ -= candidates[i]
                combo.pop()
        
        backtrack([], 0, 0)
        return res
            