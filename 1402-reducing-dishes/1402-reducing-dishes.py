class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        if satisfaction[0]>=0:
            answer=0
            for t, dish in enumerate(satisfaction):
                answer +=(t+1)*dish
            return answer
        
        min_val = float("-inf")
        length = len(satisfaction)
        
        dp = [[min_val]*length for _ in range(length+1)]
        
        #dp[t][dish] = t시점에 dish를 선택시 얻을 수 있는 max Profit
        dp[0]=[0]*length
        dp[1]=satisfaction        
        
        if length ==1:
            return max(satisfaction[0],0)
        
        for t in range(2,length+1):
            for dish in range(1,length):
                dp[t][dish]=max(dp[t][dish],dp[t-1][dish-1])+satisfaction[dish]*t
        
        return max(list(zip(*dp))[length-1])  
            