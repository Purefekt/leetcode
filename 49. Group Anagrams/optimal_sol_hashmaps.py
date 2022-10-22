"""
For each word, create a count of every lowercase english letter. To do this create a list of size 26 for each word. 
Index 0 is a and index 25 is z. Initialize all to 0 and iterate through all characters and increment.
Use this list as the key of the hashmap and the value will be a list of all words which have the same counts.
Result will be a list of all the values of the hashmap

O(NK) time where n is the number of strings in the input and k is the length of the longest string
O(N) space since in the worst case none of the words are anagrams of each other. Thus we will store n keys in the hashmap and result will have n elements.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        for word in strs:
            curr_word = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                curr_word[index] += 1
            
            # convert to tuple to be hashable
            curr_word = tuple(curr_word)
            
            if curr_word not in hashmap:
                hashmap[curr_word] = [word]
            else:
                hashmap[curr_word].append(word)
        
        res = []
        for v in hashmap.values():
            res.append(v)
        
        return res
    