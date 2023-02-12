class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1,len2 = len(word1) , len(word2)
        
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        
        for i in range(1,len1+1):
            for j in range(1,len2+1):
               
                if(word1[i-1]==word2[j-1]):
                    dp[i][j]=dp[i-1][j-1]+1
                else :
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        

        return len1-dp[-1][-1]+len2-dp[-1][-1]