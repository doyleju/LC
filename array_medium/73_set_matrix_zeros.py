class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        #1 96p
        cols = set()
        
        for row, row_list in enumerate(matrix):
            clear_row = False
            for col, num in enumerate (row_list):
                if num == 0:
                    cols.add(col)
                    clear_row = True
                    
            if clear_row:
                for col, num in enumerate (row_list):
                    matrix[row][col] = 0
                    
        
        for col in cols:
            for row, _ in enumerate (matrix):
                matrix[row][col] = 0
