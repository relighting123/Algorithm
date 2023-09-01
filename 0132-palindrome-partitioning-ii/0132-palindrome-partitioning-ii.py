class Solution:
    def minCut(self, s: str) -> int:
        dp={}
        n=len(s)
        #[1] 주어진 문자에 대해 모든 회문을 찾는다
        if n==1:
            return 0
        for i in range(n):
            dp[(i, i)] = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[(i, i + 1)] = 1

        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                if s[i] == s[j] and dp.get((i + 1, j - 1), False):
                    dp[(i, j)] = 1
        
        #print(dp)
        
        cnt_palindrome={}
        #[3] 최단 거리 탐색
        
        for i in range(1,len(s)):
            if (0,i) not in dp:
                dp[(0,i)]=dp[(0,i-1)]+1
        #print(dp)
        for i in range(1,len(s)):
            for k in range(1,i+1):
                if (k,i) in dp:
                    dp[(0,i)]=min(dp[(k,i)]+dp[(0,k-1)],dp[(0,i)])
        #print(dp)
        return dp[(0,n-1)]-1
                