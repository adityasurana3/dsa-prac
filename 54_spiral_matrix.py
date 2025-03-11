from typing import List


class Solution:
    '''
    Example 1:

    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:

    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    '''

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        up = 0
        down = rows - 1
        left = 0
        right = cols - 1
        count = 0
        mat = []
        while (count < rows*cols):
            # traverse from left to right
            for row in range(left, right+1):
                mat.append(matrix[up][row])
                count += 1

            # traverse from up to down
            for col in range(up + 1, down+1):
                mat.append(matrix[col][right])
                count += 1
            if down != up:
                # traverse from right to left
                for row in range(right - 1, left-1, -1):
                    mat.append(matrix[down][row])
                    count += 1

            if right != left:
                # traverse from down to up
                for col in range(down-1, up, -1):
                    mat.append(matrix[col][left])
                    count += 1

            up += 1
            down -= 1
            left += 1
            right -= 1
        return mat


s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

#  [1,2,3,4,8,12,11,10,9,5,6,7]
