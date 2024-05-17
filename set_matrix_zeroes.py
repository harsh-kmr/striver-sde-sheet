# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        column_0 =1
        for i in range(n):
            for j in range(m):
                if j == 0:
                    if matrix[i][j] == 0:
                        column_0 = 0
                        continue
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
    
        for i in range(1,n):
            for j in range(1,m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0 
        if matrix[0][0] == 0:
            for j in range(1,m):
                matrix[0][j] = 0
        if column_0 == 0:
            for i in range(n):
                matrix[i][0] = 0
