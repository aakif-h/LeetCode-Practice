class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])
        set_first_row = set_first_col = False
        for i in range(n):
            for j in range(m):    
                if matrix[i][j] == 0:
                    if i == 0:
                        set_first_row = True
                    if j == 0:
                        set_first_col = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        for i in range(1,n):
            for j in range(1,m):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if set_first_row:
            for j in range(m):
                matrix[0][j] = 0
        if set_first_col:
            for i in range(n):
                matrix[i][0] = 0
        return matrix
