"""
Sort + Binary search.
Sort the input.
Create a prices list, we will perform binary search over this.
Create a max beauty list, this is a list which tells the max beauty till a given idx.
beauty_max[i] = max beauty value till and including idx i.
Iterate over queries, find the max index possible by running binary search over prices.
Get the max beauty for that index.

O(nlogn + mlogm) time where n is size of items and m is size of queries. Sorting items takes nlogn time. Then iterating over queries takes m time and we run binary search each time which takes logm time.
O(n) space used by sorting input.
"""

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort()

        prices = [p for p,b in items]
        beauty = [b for p,b in items]
        beauty_max = []
        cur = 0
        for b in beauty:
            cur = max(cur, b)
            beauty_max.append(cur)

        def bin_search(q):
            l = 0
            r = len(prices)-1
            res = -1
            while l<=r:
                p = (l+r)//2
                if prices[p] <= q:
                    res = max(res, p)
                    l = p+1
                else:
                    r = p-1
            return res

        # get the max index for current query price
        res = []
        for q in queries:
            max_idx = bin_search(q)
            if max_idx == -1:
                res.append(0)
            else:
                res.append(beauty_max[max_idx])
        
        return res
