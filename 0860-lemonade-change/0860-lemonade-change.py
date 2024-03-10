class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens, twenties = 0, 0, 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                elif fives >= 1:
                    fives -= 1
                tens += 1
            elif bill == 20:
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                    twenties += 1
                else:
                    return False
        
        return True