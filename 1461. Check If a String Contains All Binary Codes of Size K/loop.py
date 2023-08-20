"""
A binary string of size k can represent 2^k values.
Go through all substrings of size k and add it to a set.
If the size of this set == 2^k, means we have found all possible values.

O(n*k) where n is the size of s. We loop through s and treat each index as the start of the substring. Creating the substring of size k takes O(k) time as well.
O(2^k) to store all possible representations in the set
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        # go through all substrings of size k and add them to a set
        unique_substrings = set()

        for i in range(len(s) - k + 1):
            unique_substrings.add(s[i:i+k])
        
        if len(unique_substrings) != 2**(k):
            return False
        return True
