class Solution(object):
    def findTargetSumWays(self, nums, target):
        """        
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        maxval,minval = sum(nums),abs(sum(nums))*(-1)
        dp = {}
        
        for t in range(minval,maxval+1):            
            dp[t] = [0]
            if t == nums[0]:
                dp[t][0] += 1
            if t == -nums[0]:
                dp[t][0] += 1
                
        for i in range(1,len(nums)):
            for t in range(minval,maxval+1):
                dp[t].append(0)
                if t-nums[i] >= minval:
                    dp[t][-1] += dp[t-nums[i]][i-1]
                if t+nums[i] <= maxval:
                    dp[t][-1] += dp[t+nums[i]][i-1]
        
        return dp[target][-1] if target in dp else 0