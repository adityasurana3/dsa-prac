from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while(i < j):
            result = numbers[i] + numbers[j]
            if result == target:
                return [i, j]
            elif result > target:
                j -= 1
            else:
                i += 1
        return []
    
        ################## Brute force approach[O(n^2)] ##########################
        '''
        total_len_of_nums = len(numbers)
        for i in range(total_len_of_nums):
            for j in range(i+1, total_len_of_nums):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return []
        '''
                
                
s = Solution()
result = s.twoSum(numbers = [2,7,11,15], target = 9)
print(result)
