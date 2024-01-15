"""
Create hashmap of losses for all players.
For win, add 0 and for loss add 1.
Create 2 lists, unbeaten and lost one.
Add all keys to unbeaten where values are 0 and add all keys to lost one where values are 1.
Sort both and return.

O(nlogn) time. n time to build the hashmap, n time to build both lists and nlogn time to sort each.
O(n) space used by the hashmap.
"""

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        losses = collections.defaultdict(int)

        for win, loss in matches:
            losses[win] += 0
            losses[loss] += 1
        
        unbeaten = []
        lost_one = []

        for k,v in losses.items():
            if v == 0:
                unbeaten.append(k)
            elif v == 1:
                lost_one.append(k)
        
        unbeaten.sort()
        lost_one.sort()

        return [unbeaten, lost_one]
