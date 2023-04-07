class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #dp[i][j] : j번째 값을 사용 혹은 사용시 i 달성 여부
        max_t = sum(nums)
        if max_t%2 !=0:
            return False
        n = len(nums)
        dp=[[False]*n for _ in range(1+max_t/2)]
        
        for j in range(n):
            dp[0][j]=True
        
        for j in range(n):
            for i in range(1+max_t/2):
                
                
                if dp[i][j-1] == True:
                    dp[i][j] = True
                if i-nums[j] >=0 and dp[i-nums[j]][j-1] == True:
                    dp[i][j] = True
                if dp[max_t/2][j]:
                    return True
                    
        return False
    
            
        
        