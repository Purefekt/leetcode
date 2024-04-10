"""
Simulate how we want the cards to be revealed.
Sort the deck since we want this order to be revealed.
Initialize res arr to the size of deck.
Create an array which holds all the indexes, for deck of size 7, it holds [0,1,2,3,4,5,6] initially.
Keep a pointer i = 0, this will track the next number in sorted deck.
First take the index at the start of the queue ie pop from left. The current element at i will be placed at this index.
Next take the next index ie pop from left and place it to the end of the queue.
Increment i.
Repeat this till we complete result.

O(nlogn) time for sorting. Queue takes n time.
O(n) space used by sorting.
"""

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()
        res = [0] * len(deck)
        index_q = [i for i in range(len(deck))]

        i = 0
        while i < len(deck):
            idx_in_res = index_q.pop(0)
            res[idx_in_res] = deck[i]
            
            if index_q:
                idx_move_behind = index_q.pop(0)
                index_q.append(idx_move_behind)

            i += 1
        
        return res
