class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        carry = 0
        for i in range(len(num)-1, -1, -1):
            unit_place = k % 10
            k = k // 10
            val = num[i] + unit_place + carry
            carry = val // 10
            val = val % 10

            num[i] = val
        
        while k > 0:
            val = k % 10 + carry
            carry = val // 10
            val = val % 10
            k = k // 10
            num.insert(0, val)

        if carry == 1:
            num.insert(0, 1)
        
        return num