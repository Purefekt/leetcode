class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False

        # connect s to itself to account for circular matching
        s = s + s

        # find goal in s
        for i in range(len(s) - len(goal)):
            if s[i:i+len(goal)] == goal:
                return True
        return False
