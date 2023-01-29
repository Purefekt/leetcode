"""
We know that for n=1, the sol will always be 1. Set result to '1' and start a loop from 1->n
At each step, split the current result into its groups, for example 1211 -> [1,2,11]
Next re-build res for this step, reset it to '' and for each element in res_split, add its len and the 0th element, so we add 1+1, then 1+2 then 2+1 to form 111221

O(n*m) where n is the input and m is the number of groups in each step in res
O(m+k) space. m space for res_split and k space for each intermediate result
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        
        res = '1'
        for i in range(1, n):
            # split res into groups
            c = res[0]
            res_split = []
            cur_split = ''
            for j in range(len(res)):
                if res[j] == c:
                    cur_split += res[j]
                else:
                    res_split.append(cur_split)
                    cur_split = res[j]
                    c = res[j]
            res_split.append(cur_split)
            
            # build res again
            res = ''
            for k in range(len(res_split)):
                res += str(len(res_split[k])) + res_split[k][0]
            
        return res
