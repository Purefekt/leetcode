"""
Greedy. Can go over the entire array from all points in n^2 time.
If sum of gas is less than sum of cost, return -1 since we can never make this trip
if sum of gas is more, we are gauranteed 1 valid path, so we create a diff array diff[i] = gas[i]-cost[i]
Iterate through this array, if the prefix sum is < 0, we set the result to idx+1, and reset total to 0
Since we are gauranteed a valid path, we dont need to check a cycle.

O(n) time
O(n) space to store diff array. This can be O(1) space by not maintaning the array since we only need prefix sum
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        
        total = 0
        res = 0
        for i in range(len(diff)):
            total += diff[i]

            if total < 0:
                res = i+1
                total = 0
                
        return res
        