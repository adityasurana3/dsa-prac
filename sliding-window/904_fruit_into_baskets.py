from typing import List
from collections import Counter


class Solution:
    def brute_force(self, fruits: List[int]) -> int:
        maxi = 0
        n = len(fruits)
        for i in range(0, n):
            my_set = set()
            for j in range(i, n):
                my_set.add(fruits[j])
                if len(my_set) > 2:
                    break
                maxi = max(maxi, j - i + 1)
        return maxi

    def better(self, fruits: List[int]) -> int:
        left = right = maxi = 0
        my_dict = {}
        n = len(fruits)
        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1
            while len(my_dict) > 2:
                my_dict[fruits[left]] = my_dict[fruits[left]] - 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1

            if len(my_dict) <= 2:
                maxi = max(maxi, right - left + 1)
            right += 1
        return maxi

    def totalFruit(self, fruits: List[int]) -> int:
        left = right = maxi = 0
        my_dict = {}
        n = len(fruits)
        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1
            if len(my_dict) > 2:
                my_dict[fruits[left]] = my_dict[fruits[left]] - 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1

            if len(my_dict) <= 2:
                maxi = max(maxi, right - left + 1)
            right += 1
        return maxi


s = Solution()
print(s.brute_force(fruits=[1, 2, 3, 2, 2]))
print(s.better(fruits=[1, 2, 3, 2, 2]))
