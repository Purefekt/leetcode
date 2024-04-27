"""
Top down 2d dp.
For each index of the key, we need to go to that character in the ring.
A character can be at multiple positions in the ring.
So at each index, we have n choices since a char can be at n different positions.
We will pick the closest way to go from current position to tne next.
For each position of the next char, we can either go left or right and reach it. We can create a function to get the min distance.
Recursive function takes index and current postion.
Iterate over all positions of the next char and get the least value.

O(k*r^2) time where k is the size of the key and r is the size of the ring. We run the recursive function for k*r times and for each, we loop through all positions a char has, it can have at most r positions.
O(k*r^2) space. We use k*r space for the memo cache but the call stack can reach k*r^2 space.
"""

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        def get_min_distance(a, b):
            # distance is same if we want to go from 3 to 5 or from 5 to 3, simplify it by always going from smaller to larger
            if a > b:
                a,b = b,a
            right = b - a
            left = len(ring) - right
            return min(right, left)
        
        # get locations of all chars
        locations = collections.defaultdict(list)
        for i,c in enumerate(ring):
            locations[c].append(i)

        memo = {}
        def helper(idx, cur_pos):
            if (idx, cur_pos) in memo:
                return memo[(idx, cur_pos)]

            if idx == len(key):
                memo[(idx, cur_pos)] = 0
                return 0
            
            # go to all positions for current char
            res = math.inf
            for pos in locations[key[idx]]:
                res = min(res, helper(idx+1, pos) + get_min_distance(cur_pos, pos) + 1)
            
            memo[(idx, cur_pos)] = res
            return res
        
        return helper(0, 0)
