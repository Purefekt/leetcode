"""
Top down dp.
For each book, decide weather to keep it in current shelf or put it in a new shelf.
If we keep it in a new shelf, then set current width and current height to the width and height of this book.
We can only keep it in current shelf if the addition of this book is <= shelfWidth.
So only if width + cur_width <= shelfWidth, we can try this.
We need to see if the height changes.
Memoiz on the input.

O(n*w*h) time since we make this many calls.
O(n*w*h) space used by the stack and memoiz table.
"""

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        memo = {}
        def helper(idx, cur_width, cur_height):
            if (idx, cur_width, cur_height) in memo:
                return memo[(idx, cur_width, cur_height)]
            if idx == len(books):
                return 0
            
            w, h = books[idx]
            # put in new shelf
            new = h + helper(idx+1, w, h)

            # put in cur shelf only if possible
            cur = math.inf
            if cur_width + w <= shelfWidth:
                added_height = max(cur_height, h) - cur_height
                cur = added_height + helper(idx+1, cur_width + w, cur_height + added_height)
            
            memo[(idx, cur_width, cur_height)] = min(new, cur)
            return min(new, cur)
        
        return helper(0, 0, 0)
