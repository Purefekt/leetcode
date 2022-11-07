"""
Quick_sort. This algorithm will take the pivot element and set it to its correct index in linear time.
We set the last element as the pivot and use a pointer initialized at the left end.
Iterate from left end till the end of array except for the pivot element.
At each iteration, if the ith element is greater than the pivot element, do nothing.
If the ith element is <= the pivot element, swap ith element and pointer element and increment pointer by 1.
At the end of the loop, swap pivot element and pointer element. Now the element at the pointer is in its correct index in a ascending order sorted array.
The kth largest element is also the n-kth element. If this pointer == n-k, this means we found the element. Otherwise run quickselect on either the left array or right array.
If the pointer > n-k, we shift the right to pivot-1, else we shift left to pointer+1

O(n) average time and O(n^2) worst case time.
O(1) space using in place
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        def quick_sort(l,r):
            pointer = l
            pivot = r
            
            for i in range(l,r):
                if nums[i] > nums[pivot]:
                    continue
                else:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1
            nums[pointer], nums[pivot] = nums[pivot], nums[pointer]
            
            if pointer == n-k:
                return nums[pointer]
            elif pointer < n-k:
                l = pointer+1
                return quick_sort(l,r)
            else:
                r = pointer-1
                return quick_sort(l,r)
        
        l = 0
        r = n-1
        
        return quick_sort(l,r)
        