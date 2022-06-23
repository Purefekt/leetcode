class Solution:
    def reverseWords(self, s: str) -> str:
        
        # get list of words in s
        s_list = s.split()
        s_list_rev = []
        
        print(s_list)
        
        # reverse each word in s_list
        for i in range(len(s_list)):
            
            # list of chars for current word
            word = list(s_list[i])
            # reverse current word
            l = 0
            r = len(word) - 1 
            while l<r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            # convert reversed word to string and add to s_list
            word = ''.join(word)
            s_list[i] = word
            
        
        # join s_list to a string
        s = ' '.join(s_list)
        
        return s
        