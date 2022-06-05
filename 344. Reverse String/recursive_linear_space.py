class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Recursion
        def recursive_fun(l,r):
            if l<r:
                s[l], s[r] = s[r], s[l]
                
                l = l+1
                r = r-1
                
                recursive_fun(l,r)
        
        # call the recursive func with initial values
        left = 0
        right = len(s) - 1
        recursive_fun(l=left, r=right)