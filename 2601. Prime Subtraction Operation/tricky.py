"""
Brute force, still tricky.
Greedy idea is that we need to convert any num as small as we can while still being larger than i-1.
Create a function to find the prime number which find the largest such prime number, we can go largest candidate to 2. (1 and 0 are not primes).
We only need to track the previous number, we can start with prev = 0.
Now the first number needs to be subtracted by a number less than itself so it is atleast 1.
This is because, if first number is 5, then we cannot do 5-5, even though 5 is a prime to get 0. The best candidate must be 3; 5-3 = 2.
Now prev is set to 2.
But there are cases where we need to not apply the operation and skip that num.
In such cases, the largest potential diff would be <2 and if current num is already larger than prev, we can set current to prev and move to the next number.

O(n*m*m) time where n is size of nums and m is value of largest num. Find prime runs in m^2 time. Both are <= 1000.
O(1) space.
"""

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def find_prime(largest_diff):
            for i in range(largest_diff, 1, -1):
                flag = True
                for j in range(2, i):
                    if i % j == 0:
                        flag = False
                        break
                if flag:
                    return i
            return -1

        
        # try to make num as small as possible but still larger than previous
        prev = 0
        for n in nums:
            largest_diff = (n-prev)-1

            if largest_diff < 2:
                if n <= prev:
                    return False
                prev = n
                continue

            chosen_diff = find_prime(largest_diff)
            if chosen_diff == -1:
                return False
            prev = n - chosen_diff
        
        return True
