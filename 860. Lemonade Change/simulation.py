class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        money = collections.defaultdict(int)

        for b in bills:
            money[b] += 1

            if b==5:
                continue
            
            elif b==10:
                if 5 not in money:
                    return False
                money[5] -= 1
                if money[5] == 0:
                    del money[5]
            
            elif b==20:
                if 10 in money and 5 in money:
                    money[10] -= 1
                    money[5] -= 1
                    if money[10] == 0:
                        del money[10]
                    if money[5] == 0:
                        del money[5]
                
                elif 5 in money and money[5] >= 3:
                    money[5] -= 3
                    if money[5] == 0:
                        del money[5]
                
                else:
                    return False
        
        return True
        