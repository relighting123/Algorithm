class Solution:
    def grayCode(self, n: int) -> List[int]:
        dp = [[]for i in range(max(3,n+1))]
        
        dp[0]=[]
        dp[1] =[0]
        dp[2]=["00","01","11","10"]
        if n ==1 :
            return [0,1]
        if n<=2:
            ans =[]
            for dlist in dp[n]:
                ans.append(int(dlist,2))
            return ans
        for i in range(3,n+1):
            temp=[]
            for dlist in dp[i-1]:
                temp.append("0"+dlist)
            
            temp2=[]
            for dlist in dp[i-1]:
                temp2.append("1"+dlist)
            
            dp[i]=temp+temp2[::-1]
            
            
            
        ans=[]
        for dlist in dp[n]:
            ans.append(int(dlist,2))
        return ans
        

        