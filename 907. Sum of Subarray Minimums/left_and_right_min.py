"""
For any subarray, we need to find the min element.
For each element, we need to see its influence in both left and right directions.
For the subarray [3,2,1,4], the min is 1, but it is also 1 for other subarrays of this subarray.
[3,2,1], [3,2,1,4], [2,1], [2,1,4], [1], [1,4], for all these, the min value is 1.
Thus 1 has influence till 0th index on the left and till last index on the right.
We use a monotonic increasing stack where we add the indexes of the elements and the stack is increasing in the element values.
Keep adding if the element is >= top of stack, else if current element is < top of stack, pop from stack.
Here we will find out the left and right influence of this index.
The leftmost index till where it is min is the element at the top of stack, if stack is empty then it is -1.
The rightmost index is the index it is poped at.
For (removed index - left index) * (right index - removed index) number of subarrays is the where arr[removed index] is min, thus add these many to the result.

O(n) time to push and pop all elements of the arr at most once each.
O(n) space for the stack.
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        mod = 10**9 + 7

        res = 0
        stack = []
        # add to the stack
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                removed_idx = stack.pop()
                left = -1
                if stack:
                    left = stack[-1]
                right = i
                res += (arr[removed_idx] * (removed_idx - left) * (right - removed_idx))
            
            stack.append(i)
        
        # work with remaining elements in the stack
        right = len(arr)
        while stack:
            removed_idx = stack.pop()
            left = -1
            if stack:
                left = stack[-1]
            res += (arr[removed_idx] * (removed_idx - left) * (right - removed_idx))
        
        return res % mod
