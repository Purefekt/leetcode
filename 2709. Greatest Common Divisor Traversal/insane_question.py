"""
This code gives TLE for some reason but is asymptotically correct.
The graph can be completely connected and so it can take O(n^2) time to build it and also O(n^2) edges.
A smarter way is to create new nodes which are prime numbers till max(nums).
These are the dummy nodes.
We check each pair of nums and prime numbers and create an edge if a number is divisible by a prime number.
Now we need to simply check if we have 1 single connected component by running DFS from each number in nums.
If we get more than 1 connected component, this means False.
NOTE: Get all prime numbers upto max(nums) using Sieve algorithm.

O(n*m) time where n is size of nums and m is max(nums).
O(n) space for the stack and prime number array.
"""

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        if 1 in nums:
            return False
        
        # get all prime numbers till max(nums) in O(n) time using sieve algorithm
        primes = [True] * (max(nums)+1)
        primes[0] = False
        primes[1] = False

        for i in range(2, max(nums)//2+1):
            # for each prime number, set all of its multiples to False since those cannot be primes now
            if primes[i] is True:
                j = 2 * i
                while j <= max(nums):
                    primes[j] = False
                    j += i
        # get the prime numbers
        prime_nums = []
        for i,status in enumerate(primes):
            if status is True:
                prime_nums.append(i)
        
        # create undirected edges between nums and all prime numbers if num%prime number == 0
        adj = collections.defaultdict(list)
        for n in nums:
            for p in prime_nums:
                if n%p == 0:
                    adj[n].append(p)
                    adj[p].append(n)

        # find number of connected components
        components = 0
        visited = set()
        for n in nums:
            if n not in visited:
                components += 1
                stack = [n]
                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    for child in adj[node]:
                        stack.append(child)
                    visited.add(node)

        if components > 1:
            return False
        else:
            return True 
        