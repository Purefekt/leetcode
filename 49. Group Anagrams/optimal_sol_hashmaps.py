"""
Create a hashmapm where the keys are 26 length long tuples. Index [0] == letter a and index [25] == z. Do this for all strings in the list. All the words using the same number of same letter
or anagrams will have the same exact tuple. the values will be these strings
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # hashmap, tuples of size 26:list of words
        result = {}
        
        for s in strs:
            
            # list of 0s with size 26 for all letters a-z. current_word[0] == a and current_word[25] == z
            current_word = [0] * 26 
            for c in s:
                # get the index position using ascii
                current_word[ord(c) - ord('a')] = current_word[ord(c) - ord('a')] + 1
            
            # convert current_word list to a tuple, since list cannot be used as hashmap key
            current_word = tuple(current_word)
            
            
            if current_word not in result.keys():
                result[current_word] = [s]
            else:
                result[current_word].append(s)
            
        # add all the values from result hashmap to a list
        anagrams_list = []
        for v in result.values():
            anagrams_list.append(v)
            
        return anagrams_list