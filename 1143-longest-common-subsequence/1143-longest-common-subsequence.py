class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1,len2=len(text1),len(text2)
        dp = [[0] * (len1+1) for _ in range(len2+1)]
        
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                
                if text1[i-1]==text2[j-1]:
                    #print(i,j)
                    dp[j][i]=dp[j-1][i-1]+1
                else : 
                    dp[j][i]=max(dp[j-1][i],dp[j][i-1])
       # print(dp)
        return dp[-1][-1]
        