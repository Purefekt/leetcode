"""
Solution is correct but causes MLE and passes all cases.
2d dp top down.
Instead of representing factories as 2d array, we can flatten it to create a 1d array.
Suppose factory = [[2,1], [4,2]] this becomes => [2,4,4] since 2 has limit of 1 and 4 has limit of 2, we treat it as if there are 2 factories at 4.
Sort the robots and factories. (why? see proof)
Helper function takes the robot index and factory index.
We either assign a robot to a factory and add the distance or we skip and have 0 distance.
Base case if we reach end of robot array, return 0 since we fixed all robots.
Base case if we reach end of factory array, return math.inf since we didnt fix all robots but went to the end of factories.

O(m*n + m*k + mklogmk + nlogn) time. sorting robot takes nlogn time, sorting factories takes mklogmk time. Creating factory array takes m*k time, where k is average limit of all factories. Dp part takes m*n time.
O(m*k + m*n) space. m*k used by factory array and m*n space used by memo hashmap and stack.
"""

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        robot.sort()
        # flatten factory
        flat_factory = []
        for f_pos, f_limit in factory:
            for _ in range(f_limit):
                flat_factory.append(f_pos)
        flat_factory.sort()
        factory = flat_factory.copy()

        memo = {}
        # we will update factory as we perform recursion
        def helper(r_idx, f_idx):
            if (r_idx, f_idx) in memo:
                return memo[(r_idx, f_idx)]
            if r_idx == len(robot):
                return 0
            if f_idx == len(factory):
                return math.inf
        
            # assign this robot to this factory
            assign = abs(robot[r_idx] - factory[f_idx]) + helper(r_idx+1, f_idx+1)
            # do not assign this robot to this factory
            skip = helper(r_idx, f_idx+1)
            
            memo[(r_idx, f_idx)] = min(skip, assign)
            return memo[(r_idx, f_idx)]

        return helper(0, 0)
