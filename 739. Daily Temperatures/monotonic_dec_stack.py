"""
Monotonic decreasing stack. All values in the stack are always in an increasing manner
We initialize a res array of size len(temps)
We initialize the stack with 1 element which is a tuple of 2 elements, the first temp and its index which is 0
start form the 1st index (0 indexed). Check if the current temp is > the top element in the stack, if it is then pop that element from the stack and its index and update the res array at index_popped to index_popped - i. Keep doing this till the current element temp is lower than the top element of the stack or if the stack is empty.
Then add this [temp,i] to the stack and repeat

O(n) time
O(n) space
""" 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0 for i in range(len(temperatures))]

        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                _, prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            
            stack.append((temperatures[i], i))

        return res
        