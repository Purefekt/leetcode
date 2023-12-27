"""
Binary search.
If the sum of sizes of both arrays is odd, then the median is mid. If it is even then it is (mid-1 + mid)//2.
We cannot merge the lists since that would be in O(m+n) time.
We can find all the elements which go to the left array and all the ones which go to the right array.
Suppose we have [1,2,3] and [1,2,3,4,5], the combination is [1,1,2,2,3,3,4,5], the left array is [1,1,2,2] and right array is [3,3,4,5].
In the original arrays, left is made of [1,2] from first and [1,2] from second. The remaining make the right array. The median is (rightmost in left + leftmost in right)//2.
ALGO:
determine the smaller of the 2 arrays, set it to small and set the other to large.
Append -inf to the left of both and +inf to right of both to deal with edge cases.
Set left and right pointers to the small array.
Run binary search on small array. From 0 till and including pivot is what we will assume the elements we will be using for the left array from the small array.
Suppose we have 3 elements in the small array (including -inf), and suppose the half of total is 7, this means we need to take the first 4 elements from the large array.
This is an assumption, we need to verify if the portions we took are truly part of the left array.
For this, the rightmost element in the considered portion in the small array must be smaller than the rightmost+1 element in the considered portion in the large array.
And similarly, the rightmost element in the considered portion in the large array must be smaller than the rightmost+1 element in the considered portion in the large array.
If this is true, then if the total len is even, return mean of rightmost of left array and leftmost of right array. If it is odd, then return rightmost+1 of the left array.
If this is false, then if the rightmost element in the small array is larger than rightmost+1 in large array, then move r pointer to p-1. Else move l pointer to p+1.

O(log(min(m+n))) time for binary search.
O(1) space for pointers.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        small, large = nums1, nums2
        if len(nums1) > len(nums2):
            small, large = large, small
        
        small.insert(0, -math.inf)
        small.append(math.inf)
        large.insert(0, -math.inf)
        large.append(math.inf)

        half = (len(small) + len(large))//2

        l = 0
        r = len(small)-1

        while l<=r:
            p = (l+r)//2

            rightmost_small_idx = p
            rightmost_large_idx = half - (p+1) - 1
            if small[rightmost_small_idx] <= large[rightmost_large_idx+1] and large[rightmost_large_idx] <= small[rightmost_small_idx+1]:
                if (len(small) + len(large)) % 2 != 0:
                    return min(small[rightmost_small_idx+1], large[rightmost_large_idx+1])
                else:
                    return (
                        max(small[rightmost_small_idx], large[rightmost_large_idx]) + min(small[rightmost_small_idx+1], large[rightmost_large_idx+1])
                    ) / 2
            elif small[rightmost_small_idx] > large[rightmost_large_idx+1]:
                r = p-1
            else:
                l = p+1
