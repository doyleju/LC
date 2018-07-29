class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        #1 91p
        
        all_rows = []
        
        if numRows < 1:
            return all_rows
        
        all_rows = [[1]]
        
        if numRows == 1:
            return all_rows
        
        all_rows = [[1],[1,1]]
        
        if numRows == 2:
            return all_rows
        
        this_row = []
        
        for i in range(3, numRows + 1):
            this_row.append(all_rows[i-2][0])
            
            for j in range(1, i - 1):
                this_row.append(all_rows[i-2][j-1] + all_rows[i-2][j])
                
            this_row.append(all_rows[i-2][-1])
            all_rows.append(this_row)
            this_row = []
            
        return all_rows
    
        """
        #2 91p
        all_rows = []
        
        for row in range(0,numRows):
            all_rows.append([1]*(row+1))
            if row > 1:
                for j in range(1,row):
                    all_rows[row][j] = all_rows[row-1][j-1] + all_rows[row-1][j]
        
        return all_rows
        """
        
        """
        #3
        # Any row can be constructed using the offset sum of the previous row
        #     1 3 3 1 0 
        #  +  0 1 3 3 1
        #  =  1 4 6 4 1
        def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
        """
