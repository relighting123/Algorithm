class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:      
        
        n_row = len(board[0])
        n = n_row*n_row
        t_board=[]
        temp_bar=[]
        len_val=0
        isReversed = False
        dict_idx ={}
        for i in range(n):
            len_val=len_val+1   
            temp_bar.append(i+1)
            if len_val==n_row:  
                
                temp_bar.reverse() if isReversed else temp_bar
                t_board.append(temp_bar)
                temp_bar=[]
                len_val=0
                isReversed = False if isReversed else True                
        
        t_board=t_board[::-1]
        
        for i in range(n_row):
            for j in range(n_row):
                dict_idx[t_board[i][j]]=(i,j)
        
        q=deque()
        q.append((1,n_row-1,0,0))
        visited={}
        visited[1]=True
        
        ans=0
        while q:
            #print(q)
            node = q.popleft()
            visited[node[0]]=True
            #print(visited,node)
            #print(node[0],n)
            if node[0]==n:
                return node[3]
            distance=node[3]+1
            
            for i in range(node[0]+1,min(node[0]+6,n)+1):
                
                
                col,row = dict_idx[i][0],dict_idx[i][1]
                
                if board[col][row]!=-1:
                    i=board[col][row]
                if i in visited:
                    continue
                
                
           
                q.append((i,dict_idx[i][0],dict_idx[i][1],distance))
                visited[i]=True
            
        
        return -1
            
            