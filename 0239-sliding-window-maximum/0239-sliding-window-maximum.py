class Solution:           
        
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        ans=[]
        l,p,r,n=0,0,1,len(nums)
        if k<=1:
            return nums
        if n==k:
            return [max(nums)]
        que.append(0)

 
        while r<n:
            add_val=nums[r] 
            #print("before",que,l,r,add_val)
            while que and que[0] < l:
                que.popleft()
            while que and add_val>nums[que[-1]]:
                que.pop()
            que.append(r)
            #print("after",que,l,r,add_val)
            

            if r-l==k-1: 
                l+=1
                #print("add ans",nums[que[0]])
                ans.append(nums[que[0]])
            r+=1
          
        return ans
            
            
        