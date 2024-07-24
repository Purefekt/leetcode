"""
Convert each num to string and use mapping to convert it to string of real value.
Convert this to int and create a 2d array with (real value int, original value int).
Sort across first col.
Return 2nd element from array.

O(nlogn) time. Creating the 2d array takes nlogn time since one pass over n numbers and length of each int as string is logn. Sorting also takes nlogn time.
O(n) space used by 2d array and for sorting.
"""

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        # conv nums to their real vals
        new_nums = []
        for n in nums:
            old_n = n
            n = str(n)
            new_n = ""
            for c in n:
                new_n += str(mapping[int(c)])
            new_nums.append((int(new_n), old_n))
        
        new_nums.sort(key = lambda x: x[0])
        res = [b for a,b in new_nums]

        return res
