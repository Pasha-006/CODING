class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])
        flag1=1
        for i in range(0,1):
            for j in range(0,cols):
                if matrix[i][j]==0:
                    flag1=0
        flag2=1
        for i in range(0,rows):
            for j in range(0,1):
                if matrix[i][j]==0:
                    flag2=0
        for i in range(0,rows):
            for j in range(0,cols):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0 
        for i in range(1,rows):
            if matrix[i][0]==0:
                for j in range(1,cols):
                    matrix[i][j]=0
        for j in range(1,cols):
            if matrix[0][j]==0:
                for i in range(1,rows):
                    matrix[i][j]=0
        if flag1==0:
            for i in range(0,cols):
                matrix[0][i]=0 
        
        if flag2==0:

            for i in range(0,rows):
                matrix[i][0]=0 
        print(flag1)
        print(flag2)
        
        return matrix
        
        
