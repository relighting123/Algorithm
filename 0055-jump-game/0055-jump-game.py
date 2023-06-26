class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #dp[j] : j에 도달할 수 있는지 여부
        
        n = len(nums)
        dp = [False]*n
        
        for i in range(n):
            if dp[-1]:
                return True
            
            if i==0:
                dp[i]= True 
                
            for j in range(1,nums[i]+1):
               # print(i,j,nums[i],dp)
                if i+j>=n:
                    continue
                if dp[j+i]:
                    continue
                if dp[i] :
                    #print(j+i)
                    dp[j+i] = True
                
        #print(dp)
        return dp[-1]