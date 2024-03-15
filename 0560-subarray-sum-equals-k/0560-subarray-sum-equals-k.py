class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = {}
        ans = 0
        res=0
        if max(nums)==min(nums) and  max(nums)==k:
            if k==0:
                return int((len(nums)*(len(nums)+1))/2)
            else:
                return len(nums)

        for i in range(len(nums)):
            res +=nums[i]
            if res == k:
                ans += 1
            if res not in dp:
                dp[res] = []
            dp[res].append(i)
        
        
        for key,val in dp.items():
            if key-k in dp:
                for target in val:
                    ans+=sum(x < target for x in dp[key-k])
        
        return ans