class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens, twenies = 0, 0, 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                tens += 1
                if fives:
                    fives -= 1
                else:
                    return False
            else: # b is 20
                change = b - 5
                if fives and tens:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True