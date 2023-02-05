"""
Create a 2d array of (user, time, website) and sort it according to the time
Create a hashmap of each user with the value being the websites that user explored in a chronological manner
For each user, get the combinations of 3 websites in all their paths. If a user explored 4 paths, we will have 4c3 or 4 combinations of size 3
Put each combination in a hashmap as key and the value will be a set of all users who went on that pattern combo
Now find the combos with the largest distinct users, and return the smallest one lexicographically

O(nC3) time. O(nlogn) time to sort the 2d matrix. The combinations takes nc3 time. But nc3 > nlogn. 
O(n) space to store the hashmaps
"""

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # create a 2d array of (user, time, website) and sort by time
        combined = []
        for i in range(len(username)):
            combined.append((username[i], timestamp[i], website[i]))
        combined.sort(key = lambda x:x[1])

        # get lists of websites visited per each user
        hashmap = {}
        for user, time, web in combined:
            if user not in hashmap:
                hashmap[user] = [web]
            else:
                hashmap[user].append(web)
        
        # get all the combinations visited by each user
        def combinations(res, options, combo, start):
            if len(combo) == 3:
                res.append(combo.copy())
                return
            
            for i in range(start, len(options)):
                combo.append(options[i])
                combinations(res, options, combo, i+1)
                combo.pop()
            
            return res


        freq = {}
        for k in hashmap.keys():
            combos = combinations(res=[], options=hashmap[k], combo=[], start=0)

            # for each combination, add it to the hashmap and add the user who went on that combo
            for combo in combos:
                if tuple(combo) not in freq:
                    freq[tuple(combo)] = set([k])
                else:
                    freq[tuple(combo)].add(k)
        
        # get the count for the combo with the most distinct users
        max_users = 0
        for v in freq.values():
            max_users = max(max_users, len(v))

        # get all the combos where the number of users == max_users
        candidate_results = []
        for k,v in freq.items():
            if len(v) == max_users:
                candidate_results.append(k)

        # return the lexicographically smallest pattern
        candidate_results.sort()

        return candidate_results[0]
