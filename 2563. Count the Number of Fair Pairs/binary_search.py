"""
Binary search.
Sort the array.
Now for each num, we can create the inequality lower <= x + num <= upper.
Which becomes lower-num <= x <= upper-num, rewrite as low <= x <= up.
Now for each num, we have a new range [low, up].
We can find the smallest index which is >= low and the largest index which is <= up.
So for [0,1,4,4,5,7] and lower = 3 and upper = 6.
When num = 1 (1st index), low = 2 and up = 5.
Using binary search, we get smallest index = 2 and largest index = 4 and so we can make 4-2+1 = 3 pairs.
NOTE: if num itself is part of the new range, then we will subtract by 1 since we cannot make a pair with just 1 number.
Return total pairs // 2 since we count each pair twice.

O(nlogn) time where n is size of nums. nlogn to sort, then we iterate over each num and for each, we run 2 binary searches in logn time each.
O(n) space used by sorting.
"""

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()

        def bin_search_low(low):
            # find the left most idx which is >= low
            l = 0
            r = len(nums)-1

            res = -1
            while l<=r:
                p = (l+r)//2

                if nums[p] >= low:
                    res = p
                    r = p-1
                else:
                    l = p+1
            return res
        
        def bin_search_up(up):
            # find the right most idx which is >= up
            l = 0
            r = len(nums)-1
            
            res = -1
            while l<=r:
                p = (l+r)//2

                if nums[p] <= up:
                    res = p
                    l = p+1
                else:
                    r = p-1
            return res

        # for each num, get the required lower and upper bounds
        res = 0
        for n in nums:
            low = lower - n
            up = upper - n

            # find index at low and up with binary search
            low_idx = bin_search_low(low)
            up_idx = bin_search_up(up)

            if low_idx == -1 or up_idx == -1:
                continue

            res += (up_idx - low_idx + 1)
            # remove 1 if n itself is part of the new range, since we cant make pair with a single number
            if low <= n <= up:
                res -= 1
        
        # divide by 2 since we counted all pairs twice
        return res//2
