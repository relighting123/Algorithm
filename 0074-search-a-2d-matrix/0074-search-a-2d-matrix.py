from bisect import bisect_left,bisect_right

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_col,n_row = len(matrix),len(matrix[0])
        col_list=[]
        for i in range(n_col):
            col_list.append(matrix[i][0])
        
        idx_col = bisect_left(col_list,target)
        if idx_col<len(col_list):
            if col_list[idx_col]==target :
                return True
        if idx_col-1<0 :
            idx_col=1
        t_list=[]
        for i in range(n_row):
            t_list.append(matrix[idx_col-1][i])

            
        idx_ans = bisect_left(t_list,target)
        
        if idx_ans>=n_row or idx_col>n_col:
            return False
      
        print(idx_ans)
        if matrix[idx_col-1][idx_ans]==target:
            return True
        else:
            return False
        
            
            