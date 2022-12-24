"""
Start with k=1 and check if p is still a substring of s (with those removed chars)
Stop when this conditions fails and return
To optimize, instead of checking for all k, run binary search on the removable array

O(nlogk). O(logk) binary search on removable of size at max k, for each check we need to check for substring which is at max the length of input string s of size n. Brute force is O(n*k)
O(1) space
"""

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def check_subseq(str1, str2):
            p1 = 0
            p2 = 0
            while p1<len(str1) and p2<len(str2):
                if str1[p1] == str2[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    p1 += 1
            if p2 == len(str2):
                return True
            return False
            
        res = 0
        l = 0
        r = len(removable)

        while l<r:
            pivot = (l+r)//2

            # create new_s without removed chars
            new_s = ''
            curr_removable = set(removable[:pivot+1])
            for j in range(len(s)):
                if j not in curr_removable:
                    new_s += s[j]

            if check_subseq(new_s,p) is True:
                res = pivot+1
                l = pivot+1
            else:
                r = pivot

        return res
            