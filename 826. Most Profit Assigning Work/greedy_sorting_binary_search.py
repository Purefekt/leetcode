"""
Greedy sorting and binary search.
For each difficuty, get the max profit we can have at this difficulty.
There can be a higher profit value at a lower difficulty level than current, we must consider that.
There can also be same difficulty with different profits, we only consider unique difficulties with max profit.
After getting max profit at each unique difficulty, sort it through difficulty.
Now loop through all workers, for a worker we need to find a difficulty <= worker capacity, the profit at this will be the max profit, add it to result.
Use binary search over this array to find this value.

O(mlogn + nlogn) time since the sorting takes nlogn time and we iterate over all m workers and each time to find the index takes logn time.
O(n) space used by sorting and combined hashmap and array.
"""

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        combined = {}
        for i in range(len(difficulty)):
            if difficulty[i] not in combined:
                combined[difficulty[i]] = profit[i]
            else:
                combined[difficulty[i]] = max(combined[difficulty[i]], profit[i])
        
        unique_combined = [[k,v] for k,v in combined.items()]
        unique_combined.sort()

        cur_max = 0
        for i in range(len(unique_combined)):
            cur_max = max(cur_max, unique_combined[i][1])
            unique_combined[i][1] = cur_max

        # binary search to get the max cap 
        def get_idx(cap):
            l = 0
            r = len(unique_combined)-1

            while l<=r:
                p = (l+r)//2
                if unique_combined[p][0] == cap:
                    return p
                elif unique_combined[p][0] > cap:
                    r = p-1
                else:
                    l = p+1
            
            return r
        
        res = 0
        for w_cap in worker:
            idx = get_idx(w_cap)
            # -1 idx means there is no job this worker can do
            if idx >= 0:
                res += unique_combined[idx][1]
        
        return res
