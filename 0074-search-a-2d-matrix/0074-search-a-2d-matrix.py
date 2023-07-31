from bisect import bisect_left,bisect_right

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n_col,n_row = len(matrix),len(matrix[0])
        if matrix[0][0]>target or matrix[n_col-1][n_row-1]<target:
            return False
        
        
        col_list=[]
        for i in range(n_col):
            col_list.append(matrix[i][0])
        
        idx_col = bisect_left(col_list,target)
        if idx_col<len(col_list):
            if col_list[idx_col]==target :
                return True
        
        t_list=matrix[idx_col-1]

            
        idx_ans = bisect_left(t_list,target)
        
        if idx_ans>=n_row or idx_col>n_col:
            return False
      
       # print(idx_ans)
        if matrix[idx_col-1][idx_ans]==target:
            return True
        else:
            return False
        
            
            