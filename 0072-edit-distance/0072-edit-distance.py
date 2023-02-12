class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        len1, len2=len(word1), len(word2)
        
        if(len1 ==0 or len2 ==0):
            return len1-len2 if len1>len2 else len2-len1
        
        dp = [ [0]*(len2+1) for _ in range(len1+1)]

    
        for i in range(1,len1+1):
              for j in range(1,len2+1):                    
                    if word1[i-1]==word2[j-1]:
                        if i==1 or j==1:
                            dp[i][j]=max(i-1,j-1)
                        elif i==j :
                            dp[i][j]=dp[i-1][j-1]

                        else :
                            dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1])
                    else :  
                        if i==1 or j==1:
                            dp[i][j]=max(dp[i-1][j],dp[i][j-1])+1
                        elif i==j:
                            dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                        else :
                            dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        

                        
    
        return dp[-1][-1]
    
              
              