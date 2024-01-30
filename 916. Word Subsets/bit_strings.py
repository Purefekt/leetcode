"""
Get the combined bit string for words2, this contains the highest frequency of any char in words in words2.
If words2 = ['a', 'b'], then combined bit string = [1,1,0,0,...].
Now iterate over words in words1, get the bit string for each word and see if it is a supterset of the combined words 2 bit string.
This can be checked by iterating over the bit string, if the diff of bit word1 and combined is < 0, this means it is NOT a superset.

O(a+b) time where a is size of words1 and b is size of words2.
O(1) space since bit strings are of fixed size.
"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        # create a bitstring which represents the max frequency of a char in all words in words2
        combined_bits_words2 = [0] * 26
        for w in words2:
            bit_string = [0] * 26
            for c in w:
                bit_string[ord(c) - ord('a')] += 1
            for i in range(26):
                combined_bits_words2[i] = max(combined_bits_words2[i], bit_string[i])
        
        # for each word in words1, get its bit string and compare it with combined_bits_words2
        def valid(bit_words1):
            for i in range(26):
                if bit_words1[i] - combined_bits_words2[i] < 0:
                    return False
            return True

        res = []
        for w in words1:
            bit_string = [0] * 26
            for c in w:
                bit_string[ord(c) - ord('a')] += 1
            if valid(bit_string) is True:
                res.append(w)
        
        return res
