class Solution(object):
    def findTargetSumWays(self, nums, target):
        """        
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        maxval,minval = abs(sum(nums))+abs(target),(abs(sum(nums))+abs(target))*(-1)
        dp = {}
        
        for t in range(minval,maxval+1):            
            
            if t == nums[0] or t == -nums[0]:
                dp[t]=[1] if nums[0]!=0 else [2]
            else:
                dp[t]=[0]
        
        for i in range(1,len(nums)):
            for t in range(minval,maxval+1):
                if t-nums[i] < minval or t+nums[i]>maxval:
                    dp[t].append(0)
                    continue
                
                dp[t].extend([dp[t - (nums[i])][i-1] + dp[t + (nums[i])][i-1]])
        return dp[target][-1] if target in dp else 0