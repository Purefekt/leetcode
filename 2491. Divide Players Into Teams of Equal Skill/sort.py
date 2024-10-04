"""
Sort.
First check if sum of skills is divisible by total possible teams (n//2).
If not, then return -1.
Now sort the skills array.
Make pairs by taking last and first element.
The sum should always be sum of skills / total teams.
If not then return -1.
Add the product to res.

O(nlogn) time for sort and then linear scan for 2 pointers.
O(n) space for sorting.
"""

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        total = sum(skill)
        n = len(skill)
        teams = n//2
        if total % teams != 0:
            return -1
        
        skill_per = total // teams
        skill.sort()

        l = 0
        r = n-1
        res = 0
        while l<r:
            if skill[l] + skill[r] != skill_per:
                return -1
            res += (skill[l] * skill[r])
            l += 1
            r -= 1
        
        return res
