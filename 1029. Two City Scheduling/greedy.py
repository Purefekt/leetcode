"""
Greedy. Subtract all A costs from B costs. The resulting elements tells us how favorable is it to go to B than A
The smaller the number, the better to send the person to B
Sort this array, the first n people must be send to B and last n people must be sent to A
Encode the index into B_sub_A to make this easier

O(nlogn) time to sort. 
O(n) space to sort in python. Also to store all the lists need n space per list.
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        n = len(costs)//2
        
        # get costs to A and B in 2 lists
        A, B = [], []
        for a,b in costs:
            A.append(a)
            B.append(b)
        
        # get B-A with index encoded
        B_sub_A = []
        for i in range(len(A)):
            B_sub_A.append((B[i]-A[i], i))
        
        # sort, first n must go to B and last n go to A
        B_sub_A.sort()

        to_A = B_sub_A[n:]
        to_B = B_sub_A[:n]

        res = 0
        for i in range(n):
            res += A[to_A[i][1]]
            res += B[to_B[i][1]]
        
        return res
        