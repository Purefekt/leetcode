class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = False
        last = digits[-1] + 1
        if last > 9:
            carry = True
            last %= 10
        digits[-1] = last

        if carry is True:
            for i in range(len(digits)-2, -1, -1):
                val = digits[i]
                if carry is True:
                    val += 1
                if val > 9:
                    val %= 10
                    carry = True
                else:
                    carry = False
                digits[i] = val
        
        if carry is True:
            digits.insert(0, 1)
        
        return digits
        