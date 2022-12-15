"""
Recursive dfs, backtrack
Keep adding numbers to the combo till its len is equal to len of nums
Once it hits that len, pop the last element from combo and re add it to nums (backtrack)

O(n*n!) time
O(n!) space
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []

        def dfs(combo):
            if len(combo) == n:
                res.append(combo.copy())
                return
            
            for i,v in enumerate(nums):
                combo.append(v)
                nums.pop(i)
                dfs(combo)
                combo.pop()
                nums.insert(i,v)
        
        dfs([])
        return res
        