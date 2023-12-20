"""
Sliding window with monotonic decreasing queue.
We will add indexes to the deque in a monotonically decreasing fashion.
Initialize the deque for the first sliding window by iterating over the first k indexes.
For each index, first remove all elements from the right side which are smaller than the current index element.
Then append to the right.
For example, if the window is of size 3 and the array is [1,3,1,-1], the initial deque will look like [3,1].
Add the first element of the deque[0] to result since it holds the largest element in a monotonically decreasing queue.
Now iterate from k till the end of the nums list.
First we need to remove all elements from the left of the deque whose index is <= i-k. Since these are outside the window now.
Then pop elements from the right till nums[i] >= dq[-1] to maintain decreasing order.
Finally the element at deque[0] will contain the largest element in the given window.

O(n) time since each element is popped either once or twice.
O(k) since the max size of the deque will be k.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = collections.deque()
        res = []
        # initial window
        for i in range(k):
            # keep poping from right end till nums[i] >= dq[-1]. This is to maintain monotonic decreasing.
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])

        # for the remaining windows
        for i in range(k, len(nums)):
            # remove from left side if the index is out of window
            if dq and dq[0] == i-k:
                dq.popleft()

            # keep popping from right end till nums[i] >= dq[-1].
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()            
            
            dq.append(i)
            res.append(nums[dq[0]])
        
        return res
