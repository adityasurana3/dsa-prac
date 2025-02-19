# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]

from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        sum = 0
        for i in range(row):
            first_occurance = mat[i][i]
            second_occurance = mat[i][col-i-1]
            sum += first_occurance
            if i != col-i-1:
                sum += second_occurance
        return sum
            


mat = [[1,2,3], [4,5,6], [7,8,9]]
mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
s = Solution()
print(s.diagonalSum(mat))