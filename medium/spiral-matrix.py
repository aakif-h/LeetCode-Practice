class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if matrix == []:
            return []
        
        if len(matrix) == 1:
            return matrix[0]
        
        #if len(matrix[0]) == 1:
            
            
        
        ans = [0]*len(matrix)*len(matrix[0])
        
        top = True
        left = right = bottom = False
        
        min_col = min_row = 0
        max_col = len(matrix[0])-1
        max_row = len(matrix)-1
        #print(corner1, corner2, corner3, corner4)

        k = 0
        while min_col <= max_col and min_row <= max_row:
            for col in range(min_col, max_col+1):
                ans[k] = matrix[min_row][col]
                k += 1
            for row in range(min_row+1, max_row+1):
                print(row, max_col, k)
                ans[k] = matrix[row][max_col]
                k += 1
            if min_col < max_col and min_row < max_row:
                for col in range(max_col-1, min_col, -1):
                    ans[k] = matrix[max_row][col]
                    k += 1
                for row in range(max_row, min_row, -1):
                    ans[k] = matrix[row][min_col]
                    k += 1
            min_row += 1
            max_row -= 1
            min_col += 1
            max_col -= 1
        
        return ans
                
        
