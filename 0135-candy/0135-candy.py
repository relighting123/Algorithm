class Solution:
    def candy(self, ratings: List[int]) -> int:
        def empty_queue(queue,cnt_prevCandy,ans):
            j,n,temp_val=1,len(queue),0
            while queue:
                temp_val = j
                queue.popleft()
                j+=1
                ans+=temp_val
            ans-=min(cnt_prevCandy,temp_val)
            queue=deque([])
            return ans
        
        
        queue,i,n,cnt_prevCandy,ans=deque(),0,len(ratings),0,0 
        
        
        for i in range(1,n):
            prev_val,cur_val=ratings[i-1],ratings[i]
            if cur_val>=prev_val:
                if i==1:
                    cnt_prevCandy=1
                    ans+=1
                if queue:
                    queue.append(cur_val)
                    ans=empty_queue(queue,cnt_prevCandy,ans)  
                    cnt_prevCandy=1
                    
            #오름차순인 경우 i-1번쨰 캔디 갯수를 을 list에 저장함. 캔디 갯수를 이전 갯수 +1 진행함.
            if cur_val>=prev_val:
                cnt_prevCandy= cnt_prevCandy+1 if cur_val>prev_val else 1
                ans+=cnt_prevCandy
                
            #내림차순인 경우 
            elif cur_val<prev_val:
                queue.append(prev_val)
                if i==n-1:
                    queue.append(cur_val)
                    ans=empty_queue(queue,cnt_prevCandy,ans)  
                    cnt_prevCandy=1
                
        if n==1:
            return 1
        return ans