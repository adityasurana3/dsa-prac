
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Solution 1
        transpose = []
        row = len(matrix)
        col = len(matrix[0])
        transpose = [[0]*row for i in range(col)]
        for i in range(row):
            for j in range(col):
                transpose[j][i] = mat[i][j]
        return transpose
    
        # Solution 2
        '''
        if not matrix:
            return []
        
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        '''

                


mat = [[1,2,3],[4,5,6],[7,8,9]]
# mat = [[1,2,3],[4,5,6]]

s = Solution()
print(s.transpose(matrix=mat))