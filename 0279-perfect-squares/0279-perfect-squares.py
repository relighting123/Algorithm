class Solution(object):
    def numSquares(self, n):
        inf = float("inf")
        sqrt_list =[i*i for i in range(1, int(n**0.5)+1)]
        dp =[inf for i in range(n+1)]
        dp[0]=1
        for i in range(n+1):
            if  int(i ** 0.5) ** 2 == i:
                dp[i]=1
                continue
            for j in sqrt_list:    
                dp[i]=min(dp[i],dp[i-j]+dp[j]) 
        return dp[-1]