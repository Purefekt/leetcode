"""
2 Queues.
Each senator should pick the next closest opposing senator to ban.
Use 2 queues, one for R and one for D. Add the senator indexes to the corresponding queue.
Now perform the bans till one party is completely wiped out.
While loop till both queues exists, pop the left most senator from both R and D, and compare their indexes,
the senator with higher index will be banned and the one with the lower index will be added to the right end of the queue with a new index which is current index + len(senate).
Return the party name whose queue still exists.

O(n) time. n time to build the 2 queues and n time for voting.
O(n) space for the queues
""" 

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        R = collections.deque()
        D = collections.deque()

        senate = list(senate)

        for i, s in enumerate(senate):
            if s == 'R':
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            R_idx = R.popleft()
            D_idx = D.popleft()

            if R_idx < D_idx:
                R.append(R_idx + len(senate))
            else:
                D.append(D_idx + len(senate))
        
        if R:
            return "Radiant"
        if D:
            return "Dire"
            