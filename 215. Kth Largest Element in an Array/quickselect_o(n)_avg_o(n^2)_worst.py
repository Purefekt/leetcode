"""
Use quicksort to sort only the pivot element in its correct index.
set the right most element to the pivot. Go through the array excluding the last element and maintain a pointer variable starting at left end.
if the current num is larger than the pivot, do nothing, else swap the current element with pointer element and increment pointer by 1.

At the end of this loop, swap the element at pointer index with the pivot element. Now the pivot element is at its sorted index and all elements smaller to it are at its left and all elements larger than it are on its right.

kth largest element is also the len(nums)-k element. Thus if the pivot element (now at pointer index) is equal to len(nums)-k thus we have found it and we can return nums[pointer].
If len(nums)-k > pointer index, then we run quicksort on the right subarray
else we run quisort on the left subarray

O(n) average time and O(n^2) worst time. O(1) space since swapping is in place.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick_sort(l,r):
            pivot = r
            pointer = l
    
            for i in range(l, r):
                if nums[i] > nums[pivot]:
                    continue
                elif nums[i] <= nums[pivot]:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            # finally swap pivot element and element at pointer position
            nums[pointer], nums[pivot] = nums[pivot], nums[pointer]
                
            if len(nums)-k == pointer:
                return nums[pointer]
            elif len(nums)-k > pointer:
                l = pointer+1
                return quick_sort(l,r)
            elif len(nums)-k< pointer:
                r = pointer-1
                return quick_sort(l,r)
        
        l = 0
        r = len(nums)-1
        
        return quick_sort(l,r)
    