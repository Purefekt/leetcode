class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        if k == 0:
            return [0] * len(code)

        circular_code = code.copy()
        circular_code.extend(code)
        if k > 0:
            res = []
            for i in range(len(code)):
                total = 0
                for j in range(i+1, i+k+1):
                    total += circular_code[j]
                res.append(total)
            return res
        
        else:
            res = []
            for i in range(len(code), len(circular_code)):
                total = 0
                for j in range(i-1, i+k-1, -1):
                    total += circular_code[j]
                res.append(total)
            return res
