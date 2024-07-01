class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        first = [c for c in first]
        second = [c for c in second]
        third = [c for c in third]
        first = set(first)
        second = set(second)
        third = set(third)

        res = []
        for w in words:
            chosen_set = None
            if w[0].lower() in first:
                chosen_set = first
            elif w[0].lower() in second:
                chosen_set = second
            else:
                chosen_set = third
            i = 1
            while i < len(w):
                if w[i].lower() not in chosen_set:
                    break
                i += 1
            
            if i == len(w):
                res.append(w)
        
        return res
