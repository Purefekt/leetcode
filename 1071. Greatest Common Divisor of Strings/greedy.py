"""
Take the smaller of the two strings and try differenct lengths of it to make it divide both str1 and str2.
Since we want the greatest common divisor, instead of taking [:1], then [:2], we can start from the end and take [:len(str)], [:len(str)-1].
Before trying to create str1 and str2 from current string, first check if its valid.
If len(str1) == 6 and the len(cur_string) == 4, we know we can never make str1 from cur_string since 6%4 != 0. Thus proceed only if it makes sense for both strings.
Next create both strings using cur_string * len(str)//len(cur_string).
If both are correctly formed, then return it.

O(min(n,m)*(n+m)) time where n is length of str1 and m is length of str2. We are comparing with the smaller of the two strings and in each iteration we need to build the strings for both str1 and str2.
O(min(n,m)) for copy of current_string which is the base
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        testing_string = None
        if len(str1) < len(str2):
            testing_string = str1
        else:
            testing_string = str2
        
        # try for max size till smallest size
        for i in range(len(testing_string), 0, -1):
            # check if it is compatible with both string
            if len(str1)%i != 0 or len(str2)%i != 0:
                continue
            
            cur_string = testing_string[:i]
            # build both strings
            cur_str1 = cur_string * (len(str1)//i)
            cur_str2 = cur_string * (len(str2)//i)

            if cur_str1 == str1 and cur_str2 == str2:
                return cur_string
        
        return ""
