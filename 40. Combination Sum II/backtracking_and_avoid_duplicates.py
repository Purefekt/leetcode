"""
Sort the candidates, this will be useful in avoiding duplicates
Use backtracking to build all the solutions, avoid exploring paths which have sum > target or which lead to duplicate results
Recursive function takes the current combination, the total sum of that combination and index we are at
Base case when sum = target, add to result and return or if sum > target, return
Loop through the remaining array starting at idx and add to combo and search. Keep a var prev, this will let us avoid taking the same num if candidates[idx] = prev

O(n*2^n) time. 2^n to build the search space and n time to copy the combination
O(n) space for sorting and stack
""" 

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []

        def backtrack(combo, summ, idx):
            if summ == target:
                res.append(combo.copy())
                return
            
            if summ > target:
                return
            
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] != prev:
                    combo.append(candidates[i])
                    summ += candidates[i]
                    backtrack(combo, summ, i+1)
                    combo.pop()
                    summ -= candidates[i]

                    prev = candidates[i]
        
        backtrack([], 0, 0)
        return res
        