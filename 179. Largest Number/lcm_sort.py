"""
Greedy. Sort with lcm.
We cannot simply convert to string and sort.
Take this case [6, 67]. If we convert to string and sort in reverse, we get ["67", "6"] and thus we get 676, which is correct.
But using the same strategy, take the case [6, 65], we get ["65", "6"] and we get 656, but answer is 665.
We can take the lcm of the sizes of all numbers.
Then transform all numbers to match the size of lcm by repeating themselves.
Suppose we have [1, 23, 456], taking the lcm of lengths gives us 6.
Thus we get ["111111", "232323", "456456"].
Now when we sort in reverse, we get ["456456", "232323", "111111"].
Now build the result using this order BUT use the original nums and not the transformed ones. We need to track indexes to original nums.
We build res -> 456231 which is correct.

O(nlogn) time. n time to make idx_to_num hashmap, n time to get lcm, n time to get transformed and nlogn to sort it. 
O(n) space.
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        if len(nums) == 1:
            return str(nums[0])
        
        # convert all nums to str, also create a hashmap of index to original number string
        idx_to_num = {}
        nums_str = []
        for i,n in enumerate(nums):
            nums_str.append(str(n))
            idx_to_num[i] = str(n)
        
        # get lcm of all the lengths of all nums
        # get lcm of first 2 numbers and then the rest
        len1 = len(nums_str[0])
        len2 = len(nums_str[1])
        lcm = (len1 * len2) // math.gcd(len1, len2)
        for i in range(2, len(nums_str)):
            len_i = len(nums_str[i])
            lcm = (lcm * len_i) // math.gcd(lcm, len_i)

        # for all the num strings, make them the size of the lcm by repeating themselves. For 1234, 987, lcm is 12 and so we get 123412341234 and 987987987987. Maintain indexes
        transformed = []
        for i,n in enumerate(nums_str):
            new_num = n * (lcm // len(n))
            transformed.append((new_num, i))
        
        # sort this in reverse and build the result using the original nums
        transformed.sort(reverse=True)
        res = []
        for _, idx in transformed:
            res.append(idx_to_num[idx])
        
        # edge case where largest number is 0
        if res[0][0] == "0":
            return "0"
        
        return ''.join(res)
