"""
First check if 's' and a word are even compatible. Do this by compressing all groups in a word to a single occurance and check if they are the same. If they are not then they arent compatible. For ex, heeellooo -> helo, hello -> helo, hellok -> helok
Next break 's' and the word into a list of their groups. For each ith element, if the length os s[i] and word[i] is the same or if length of s[i]>=3 AND the length of s[i]>=word[i], then that group matches. Do this for all groups, if this condition fails at any point, then return False, if all pass then True.
Count the number of True's

O(m*n) where m is the number of groups in the string s and n is the number of words in words
O(m) where m is the number of groups string s
"""

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def compress_word(word):
            cur_c = word[0]
            compressed_word = word[0]
            for i in range(1, len(word)):
                if word[i] == cur_c:
                    continue
                else:
                    cur_c = word[i]
                    compressed_word += cur_c
            return compressed_word
        
        def break_word_in_groups(word):
            cur_c = word[0]
            group = []
            start = 0
            for i,c in enumerate(word):
                if c == cur_c:
                    continue
                else:
                    group.append(word[start:i])
                    cur_c = word[i]
                    start = i
            group.append(word[start:i+1])
            
            return group
        
        def check_validity(s_group, word_group):
            for i in range(len(s_group)):
                if (len(s_group[i])==len(word_group[i]) or len(s_group[i])>=3) and (len(s_group[i])>=len(word_group[i])):
                    continue
                else:
                    return False
            return True
        
        
        
        compressed_s = compress_word(s)
        s_group = break_word_in_groups(s)
        res = 0
        for word in words:
            compressed_word = compress_word(word)
            if compressed_word != compressed_s:
                continue
            else:
                word_group = break_word_in_groups(word)
                if check_validity(s_group, word_group) is True:
                    res += 1
        
        return res
