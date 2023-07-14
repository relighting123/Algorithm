class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        a= candidates
        a.sort()

        dp = [ [] for _ in range(target+1)]
        dp_idx =[[] for _ in range(target+1)]
        
        for i in range(target+1):
            for idx,element in enumerate(a):
                if i-element<0:
                    break
                if i==element and [element] not in dp[i] :
                    dp[i].append([element])
                    dp_idx[i].append([idx])
                    #print(dp)
                
            
                for k,dplist in enumerate(dp[i-element]):
                    subans= dp[i-element][k]
                                   
                    if idx>dp_idx[i-element][k][0]:
                        
                        next_dp=subans+[element]
                        if next_dp in dp[i]:
                            continue
                        dp[i].append(next_dp)
                        dp_idx[i].append([idx])
                    
        return dp[target]