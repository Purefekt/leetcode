class Solution:
    def average(self, salary: List[int]) -> float:
        
        min_s = min(salary)
        max_s = max(salary)

        total = 0
        for s in salary:
            if s not in [min_s, max_s]:
                total += s
        
        return total / (len(salary)-2)
