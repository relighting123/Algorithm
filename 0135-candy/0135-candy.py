class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        def empty_queue(queue,list_ans,cnt_prevCandy,flag,last_acsidx):
            #print("Queue 비우기",queue)
            j=1
            n=len(queue)
            temp_list=[]
            while queue:
                temp_list.append(j)
                queue.popleft()
                j+=1
            temp_list.reverse()
            #print("temp_list",temp_list)
            if flag=="asc" and list_ans[-1]>temp_list[0]:
                list_ans=list_ans+temp_list[1:]
            else:
                list_ans=list_ans[:-1]+temp_list
            #print("Queue 비우기 완료",list_ans)
            return list_ans
        
        
        curval=0
        ans=0
        list_ans=[]
        queue=deque()
        i=0
        n=len(ratings)
        cnt_prevCandy=0
        flag=""
        last_acsidx=0
        for i in range(1,n):
           # print(i)
            prev_val,cur_val=ratings[i-1],ratings[i]
            
            #오름차순인 경우 i-1번쨰 캔디 갯수를 을 list에 저장함. 캔디 갯수를 이전 갯수 +1 진행함.
            if cur_val>prev_val:
                if i==1:
                    cnt_prevCandy=1
                    list_ans.append(cnt_prevCandy)
                    
                if queue:
                    queue.append(cur_val)
                    list_ans=empty_queue(queue,list_ans,cnt_prevCandy,flag,last_acsidx)  
                    queue=deque([])
                    cnt_prevCandy=1
                
                cnt_prevCandy= cnt_prevCandy+1
                list_ans.append(cnt_prevCandy)
                flag="asc"
                last_acsidx=i
                
                #print("오름차순",i,list_ans,queue)
            
            #내림차순인 경우 
            elif cur_val<prev_val:

                queue.append(prev_val)
                if i==n-1:
                    queue.append(cur_val)
                    list_ans=empty_queue(queue,list_ans,cnt_prevCandy,flag,last_acsidx)  
                    queue=deque([])
                    cnt_prevCandy=1
                    
                #print("내름차순",i,list_ans)
                    
                            
            
            #전/후 동일한 경우 내림차순 queue 내 값을 활용하여 list_ans 업데이트하고 초기화 flag를 전달함.
            else :
                #print("동일값")
                if i==1:
                    cnt_prevCandy=1
                    list_ans.append(cnt_prevCandy)
                if queue:
                    queue.append(cur_val)
                    list_ans=empty_queue(queue,list_ans,cnt_prevCandy,flag,last_acsidx)  
                    queue=deque([])
                    cnt_prevCandy=1
                list_ans.append(1)
                cnt_prevCandy=1
                flag="same"
        #print(list_ans)
        if n==1:
            return 1
        return sum(list_ans)