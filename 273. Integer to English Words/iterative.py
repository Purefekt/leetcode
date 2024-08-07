"""
Just annoying.
Did iteratively.
"""

class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"
        
        hashmap = {
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen",
            "20": "Twenty",
            "30": "Thirty",
            "40": "Forty",
            "50": "Fifty",
            "60": "Sixty",
            "70": "Seventy",
            "80": "Eighty",
            "90": "Ninety"
        }

        # for each set of 3 numbers, figure out the last 2 
        num = str(num)
        num = num[::-1]
        # place in separate bins
        bins = []
        l = 0
        for r in range(len(num)):
            if r%3 == 0:
                bins.append(num[l:r])
                l = r
        bins.append(num[l:r+1])
        bins.pop(0)
        bins = bins[::-1]
        for i in range(len(bins)):
            bins[i] = bins[i][::-1]
        
        # convert to value for each upto 3 digit string in bins
        def convert_three_digit(s):
            # get rid of leading zeros
            s = int(s)
            s = str(s)
            if s == "0":
                return ""
            res = []
            if len(s) == 3:
                res.append(hashmap[s[0]])
                res.append("Hundred")
                s = s[1:]
                s = int(s)
                s = str(s)
            if int(s) <= 20 and int(s) > 0:
                res.append(hashmap[s])
            else:
                if int(s) > 0:
                    tens = s[0] + "0"
                    res.append(hashmap[tens])
                    if s[1] != '0':
                        res.append(hashmap[s[1]])
            return ' '.join(res)
        
        # get the three digit value for each bin and add billion, million, thousand where needed
        size = len(bins)
        res = []
        for b in bins:
            res.append(convert_three_digit(b))
            if size == 4 and res[-1] != '':
                res.append('Billion')
            elif size == 3 and res[-1] != '':
                res.append('Million')
            elif size == 2 and res[-1] != '':
                res.append('Thousand')
            size -= 1
        
        # remove any empty strings and inter
        final_res = []
        for r in res:
            if r != '':
                final_res.append(r)
        
        return ' '.join(final_res)
        