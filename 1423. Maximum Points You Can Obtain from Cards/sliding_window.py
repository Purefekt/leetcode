"""
Sliding window.
NOTE: Everything OUTSIDE the sliding window are the cards we keep.
Create an initial sliding window of size len(cardPoints)-k by setting l->0 and r->len(cardPoints)-k-1.
The remaining cards are the ones we decide to keep, which is just the remaining cards on the right side.
Set this to window_sum and also max_sum (result).
Now move the window by 1 till the right side hits the end. When we move the window, we include the left card where we moved the window and remove the card at the right end which we added to the window.

O(k) time. O(k) time. k time to get the initial window_sum by iterating over the last k cards and k time to move the sliding window k times.
O(1) space to store l, r, window_sum in constant space.
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        l = 0
        r = len(cardPoints)-k-1

        window_sum = 0
        for i in range(len(cardPoints)-k, len(cardPoints)):
            window_sum += cardPoints[i]
        max_sum = window_sum
        

        # move the sliding window
        for _ in range(k):
            l += 1
            r += 1
            # add left side and remove right side
            window_sum += cardPoints[l-1]
            window_sum -= cardPoints[r]

            if window_sum > max_sum:
                max_sum = window_sum
        
        return max_sum
