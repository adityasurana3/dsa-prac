from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        n = len(bills)
        for bill in range(0, n):
            if bills[bill] == 5:
                five += 1
            elif bills[bill] == 10:
                if five >= 1:
                    ten += 1
                    five -= 1
                else:
                    return False
            else:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


s = Solution()
print(s.lemonadeChange(bills=[5, 5, 10, 10, 20]))
