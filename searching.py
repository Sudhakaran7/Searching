import numpy as np
class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False
val=Solution()
R,C,target=map(int,input().split())
nums=list(map(int,input().split()))
matrix=np.array(nums).reshape(R,C)
print(val.searchMatrix(matrix,target))
