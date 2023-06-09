"""
Sort and 2 pointer
Sort the products list to club all prefixes together in a sorted fashion.
maintain a left pointer and right pointer. Init at 0 and len(products)-1 respectively.
iterate over the chars in searchWord, at each iteration check if the left pointer and right pointer words are still valid.
Thus first always adjust the pointers. If the length of the word at the pointer is smaller than the index or if the the char at the index isnt the char of the searchword, then it is invalid and update the pointer
Once we have a valid window, get the first 3 words from the left pointer (or min of window size)

O(nlogn + n*w) time. nlogn to sort, n*w to update the pointers
O(logn) space to sort.
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        res = []
        l = 0
        r = len(products)-1

        for i,c in enumerate(searchWord):

            # adjust pointers
            while l<=r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l<=r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            
            this_res = []
            window_size = r-l+1
            for j in range(min(3, window_size)):
                this_res.append(products[l+j])
            
            res.append(this_res)
        
        return res
        