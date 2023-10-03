class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #dp[i]: t가 i인 시점의 최대 profit
        S=0
        P=1
       
        dp=defaultdict(int)
        info=defaultdict(list)
        for i in range(len(startTime)):
            info[endTime[i]].append([startTime[i],profit[i]])
       # print(info)
        lastidx=0
        endTime.sort()
        list_endTime=[0]
        for i in endTime:
            #print(i,dp)
            #dp[i]=dp[i-1]
            for cand in info[i]:
               # print(cand)
                cand_s=cand[S]
                cand_p=cand[P]
                previdx=bisect_left(list_endTime,cand_s)
                if previdx<len(list_endTime) and list_endTime[previdx] != cand_s:
                    previdx-=1
                if  previdx==len(list_endTime):
                    previdx-=1
                dp[i]=max(dp[lastidx],dp[list_endTime[previdx]]+cand_p)

                list_endTime.append(i)
                lastidx=i
               # print('result',dp)
        
        return dp[endTime[-1]]
        
        
        
        