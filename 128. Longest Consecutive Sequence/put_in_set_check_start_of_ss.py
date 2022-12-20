"""
Put the input array in a set
Go through the array, for each element check is n-1 exists in the set, if it DOESNT, this means that this is the start of a consective subsequence
If it IS a start, then run a while loop and check if subsequent consecutive number is there, continue and update max ss length

O(n) time
O(n) space
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        # convert input array to set
        arr = set()
        for n in nums:
            arr.add(n)

        max_ss_len = 1
        for n in arr:
            
            if n-1 not in arr:
                ss_len = 1
                subsequent_n = n+1
                while True:
                    if subsequent_n in arr:
                        ss_len += 1
                        subsequent_n += 1
                        max_ss_len = max(max_ss_len, ss_len)
                    else:
                        break
        
        return max_ss_len
        