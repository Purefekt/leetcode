"""
Using a sliding window, we can get the subarrays where there are at most K unique numbers.
Use a count hashmap and a sliding window. Increase window and add to the hashmap.
At any point if the keys of hashmap > K, shrink the window and update count map.
Keep adding all number of valid subarrays which is r-l+1.
Find this for k(A) and k-1(B).
The result for exactly k will be A - B.

O(n) time for 2 passes over nums with k and k-1.
O(n) space, at a time the highest number of keys stored in the hashmap will be k == n.
"""

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        # Finds the number of subarrays where the number of unique numbers are at most K
        def helper(K):
            l = 0
            res = 0
            freq = collections.defaultdict(int)

            for r in range(len(nums)):
                freq[nums[r]] += 1
                # shrink
                while len(freq) > K:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                
                res += (r-l+1)
            
            return res
        
        # use helper to get value for at most k and at most k-1. Result is diff of these
        A = helper(k)
        B = helper(k-1)

        return A-B
            