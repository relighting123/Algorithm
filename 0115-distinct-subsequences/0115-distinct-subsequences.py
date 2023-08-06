from collections import defaultdict
from bisect import bisect_left

class Solution:
    def getDp_TwoPointer(self,target_list,prev_dict):
        curr_dict= defaultdict(int)
        minPrev_idx,i = min(prev_dict.keys()),0  
        l,p = minPrev_idx,target_list[0]
        partialSum = 0 
        while(i<len(target_list)):
            p=target_list[i]
            if l>=p:
                curr_dict[p]=partialSum
                i+=1
                continue
            partialSum+=prev_dict[l]
            l+=1
        return curr_dict
            
        
        
        
    def numDistinct(self, s: str, t: str) -> int:
        sCharidx= defaultdict(list)
        len_t,len_s=len(t),len(s)
        for idx,val in enumerate(s):
            sCharidx[val].append(idx)
    
        dp = [defaultdict(int) for _ in range(len(t))]
        dp[0]= collections.Counter(sCharidx[t[0]])
        ans=0
        for i in range(1,len_t):
            target_char=t[i]
            target_list = sCharidx[target_char]
            if len(target_list)==0: 
                return 0
            dp[i]=self.getDp_TwoPointer(target_list,dp[i-1])

        return sum(dp[len_t-1].values())
            

            
            
    
            
                
                
            
            
        