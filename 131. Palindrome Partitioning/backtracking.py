"""
Backtracking to build all combinations of partitionings.
For the string 'aab', we can partition it in the first step as 'a', 'aa', 'aab'
Basically at each step we take the index we are at and we can partition it by idx -> len(string)
But before we add a new string to our partition combination, we must check if it is a palindrome, for example if we have 'aa' then it is valid and we add it to the partition and continue
But if its 'ab' then we dont add it to a combination and do not continue
We stop when index == len(s)
We can optimize by maintaining a hashmap of all previously seen substrings and weather they are palindromes or not

O(n*2^n) time. The tree takens 2^n time and each time a substring takes n time to validate if it is a palindrome or not
O(2^n) space since we can have at most 2^n possible valid substrings which the palindromes hashmap will store. n time for stack as well 
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        palindromes = {}
        def check_palindrome(string):
            if string in palindromes:
                return palindromes[string]
            l = 0
            r = len(string)-1
            while l<r:
                if string[l] != string[r]:
                    palindromes[string] = False
                    return False
                l += 1
                r -= 1
            palindromes[string] = True
            return True

        res = []
        def backtrack(combo, idx):
            if idx == len(s):
                res.append(combo.copy())
                return
            
            for i in range(1, len(s)+1):
                if idx+i <= len(s):
                    if check_palindrome(s[idx:idx+i]) is True:
                        combo.append(s[idx:idx+i])
                        backtrack(combo, idx+i)
                        combo.pop()
        
        backtrack([], 0)
        return res
