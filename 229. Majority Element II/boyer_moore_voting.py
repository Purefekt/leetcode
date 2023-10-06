"""
Solving Follow up with O(1) space.
Boyer-Moore Voting Algorithm
Since we need to find all elements which appear more than n/3 times, we can only have at max 2 such elements.
For example if size is 6, then an element needs to be present more than 2 times, thus atleast 3. We can only have 2 unique elements appear 3 times each since that makes up the entire array.
Now we can use a hashmap of a fixed size of 2 to track potential candidates.
First pass will help us identify the candidates. A second pass will be requires to get the frequencies of just those candidates (which is at max 2), thus O(1) space.
Create a hashmap and follow these rules.
If a number exists in the hashmap, then increment its count by 1.
Else, If the hashmap length is < 2, then simply add that number and set its value to 1.
If the number isnt in the hashmap and the length isnt 2, then we need to go through both the keys in the hashmap and remove all k-v pairs whose value is 0.
Now, if we removed 1 or both elements from the hashmap, we simply add the current num with value 1 to the hashmap.
Else if we werent able to remove any k-v pair from the hashmap (bcos none of them had value of 0), decrement the value of both keys in the hashmap by 1.
At the end of this pass, we will have either 0, 1 or 2 elements in the hashmap which are "candidates".
Now do another pass and get the frequency of only these elements.
Return a list of all candidates whose counts were higher than n/3.

O(n) time for 2 passes of linear time.
O(1) space to store a hashmap of at max size 2.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        candidates = {}

        for n in nums:
            if n in candidates:
                candidates[n] += 1
            else:
                # n doesnt belong to the hashmap
                if len(candidates) < 2:
                    candidates[n] = 1
                else:
                    # check if there exists any index which is already 0 before decrementing
                    to_delete = []
                    for k,v in candidates.items():
                        if v == 0:
                            to_delete.append(k)
                    
                    for k in to_delete:
                        del candidates[k]
                    
                    # if we removed any elements from the hashmap, then we can simply add this key, else decrement all keys
                    if len(candidates) < 2:
                        candidates[n] = 1
                    else:
                        for k,v in candidates.items():
                            if k != n:
                                candidates[k] -= 1
        
        # now check the actual count of the candidates
        # reset
        for k in candidates:
            candidates[k] = 0
        
        threshold = len(nums)/3

        for n in nums:
            if n in candidates:
                candidates[n] += 1
        
        res = []
        for k,v in candidates.items():
            if v > threshold:
                res.append(k)
        
        return res
