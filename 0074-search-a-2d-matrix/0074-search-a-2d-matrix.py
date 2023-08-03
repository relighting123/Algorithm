from bisect import bisect_left,bisect_right

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n_col,n_row = len(matrix),len(matrix[0])
        #최솟값,최대값 기준에 존재할 수 없는 경우 정의
        if matrix[0][0]>target or matrix[n_col-1][n_row-1]<target:
            return False
        
        #첫번째 열을 행 배열로 전환하여 binary Search 대상 선정. 이를 통해 몇번째 행이 중요한지 확인
        col_list=[row[0] for row in matrix]
                
        idx_col = bisect_left(col_list,target)
        if idx_col<len(col_list) and col_list[idx_col]==target:
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
        
            
            