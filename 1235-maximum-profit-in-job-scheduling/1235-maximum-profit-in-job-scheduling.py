class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #dp[i]: t가 i인 시점의 최대 profit
        S=0
        P=1
        def find_closest_number(dic, target):
            closest_number = None

            for key in reversed(dic.keys()):
                if key <= target:
                    return key
            return None

        
        dp=defaultdict(int)
        info=defaultdict(list)
        n=max(endTime)+1           
        for i in range(len(startTime)):
            info[endTime[i]].append([startTime[i],profit[i]])
       # print(info)
        lastidx=0
        endTime.sort()
        for i in endTime:
            #print(i,dp)
            #dp[i]=dp[i-1]
            for cand in info[i]:
               # print(cand)
                cand_s=cand[S]
                cand_p=cand[P]
                dp[i]=max(dp[lastidx],dp[find_closest_number(dp,cand_s)]+cand_p)
                lastidx=i
               # print('result',dp)
        
        return dp[n-1]
        
        
        
        