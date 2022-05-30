class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if s and t have diff lens, then false
        if len(s) != len(t):
            return False
        
        # make a hashmap for each string. Each hashmap is the count of alphabets. Compare.
        else:
            dict_s = {}
            dict_t = {}
            
            for c in s:
                if c not in dict_s:
                    dict_s[c] = 1
                else:
                    dict_s[c] = dict_s[c] + 1
            
            for c in t:
                if c not in dict_t:
                    dict_t[c] = 1
                else:
                    dict_t[c] = dict_t[c] + 1
            
            if dict_s == dict_t:
                return True
            return False