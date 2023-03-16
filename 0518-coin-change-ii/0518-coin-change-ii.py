class Solution(object):
    def change(self, amount, coins):

        dp=[0 for i in range(amount+1)]
        dp[0]=1
        for coin in coins:  
            for i  in range(coin,amount+1):              
                dp[i] += dp[i-coin]
        return dp[amount] 