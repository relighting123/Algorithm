class Solution:
    def candy(self, ratings: List[int]) -> int:
        def empty_queue(queue, cnt_Candy, ans):
            n = len(queue)
            print(queue,n)
            ans += int((1 + n) * n / 2)
            ans -= min(cnt_Candy, n)
            # while queue:
            #     ans+= j
            #     queue.popleft()
            #     j+=1
            return ans

        
        
        queue,i,n,cnt_Candy,ans=deque(),0,len(ratings),0,0 
        
        
        for i in range(1,n):
            prev_val,cur_val=ratings[i-1],ratings[i]
            if cur_val>=prev_val:
                if i==1:
                    cnt_Candy=1
                    ans+=1
                if queue:
                    queue.append(cur_val)
                    ans=empty_queue(queue,cnt_Candy,ans)
                    queue = deque([])
                    cnt_Candy=1
                    
            if cur_val>=prev_val:
                cnt_Candy= cnt_Candy+1 if cur_val>prev_val else 1
                ans+=cnt_Candy
                continue
                
            if cur_val<prev_val:
                queue.append(prev_val)
                if i==n-1:
                    queue.append(cur_val)
                    ans=empty_queue(queue,cnt_Candy,ans)  
                    queue = deque([])
                    cnt_Candy=1
                continue
                
        return ans if n>1 else 1