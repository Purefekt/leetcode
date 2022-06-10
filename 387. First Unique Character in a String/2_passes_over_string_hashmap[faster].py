class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hashmap with count takes one pass over the string. Another pass to get the first element which appears once. O(n) time, O(1) space since cant exceed 26 chars
        
        hashmap = {}
        for letter in s:
            if letter not in hashmap.keys():
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1
        
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        
        return -1
        