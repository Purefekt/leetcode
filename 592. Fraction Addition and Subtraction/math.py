"""
Math.

O(n) time.
O(math.gcd) space.
"""

class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        # add a leading + if it doesnt exist for a + number at the start
        if expression[0].isnumeric():
            expression = '+' + expression
        
        # split the fractions
        l = 0
        fractions = []
        for r in range(1, len(expression)):
            if expression[r] == '+' or expression[r] == '-':
                fractions.append(expression[l:r])
                l = r
        fractions.append(expression[l:])
        
        # split them into tuples of (sign, numerator, denominator) and get all unique denominators
        unique_den = set()
        for i in range(len(fractions)):
            sign = fractions[i][0]
            num_den = fractions[i][1:].split('/')
            num = int(num_den[0])
            den = int(num_den[1])
            fractions[i] = (sign, num, den)
            unique_den.add(den)
        
        # get the lcm of denominators
        lcm = 1
        for n in unique_den:
            lcm *= n
        
        # get the numerator total after updating according to lcm denominator
        numerators = 0
        for sign, num, den in fractions:
            num *= (lcm//den)
            if sign == '-':
                num *= -1
            numerators += num
        
        final_sign = ''
        if numerators < 0:
            final_sign = '-'
            numerators *= -1
        
        comm = math.gcd(numerators, lcm)
        numerators //= comm
        lcm //= comm

        return f'{final_sign}{numerators}/{lcm}'
        