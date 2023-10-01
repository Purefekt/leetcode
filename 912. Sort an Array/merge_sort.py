"""
Merge Sort.
Break the input array by halving it till there are singular element arrays.
Then merge those arrays back in sorted order.
Do this using a function merge where there is a pointer at 0 for both left and right subarrays.
Add the smaller of the two to array and increment the pointer to the one added.

O(nlogn) time. Halving the arrays takes logn time. Merging halves takes n time. 
O(n) space for the arrays used for merging.
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(L, M, R):
            left = nums[L:M+1]
            right = nums[M+1:R+1]

            i = L
            j = 0
            k = 0

            while j<len(left) and k<len(right):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            
            # one array might end with elements left in the other, thus add those elements
            while j<len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            
            while k<len(right):
                nums[i] = right[k]
                k += 1
                i += 1
        
        def mergeSort(l, r):
            if l==r:
                return
            
            m = (l+r)//2
            mergeSort(l, m)
            mergeSort(m+1, r)
            merge(l, m, r)
        
        mergeSort(0, len(nums)-1)
        return nums
        