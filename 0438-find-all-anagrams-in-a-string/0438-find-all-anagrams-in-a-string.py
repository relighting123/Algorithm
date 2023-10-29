class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p,len_p = Counter(p),len(p)
        cnt_s = Counter(s[0:len_p])
        ans=[]
        j=len_p-1
        for i in range(len(s)-len_p+1):
            if cnt_s==cnt_p:
                ans.append(i)
                
                
            j+=1
            if j>=len(s):
                break
            cnt_s[s[j]]+=1       
            cnt_s[s[i]] -=1
            if cnt_s[s[i]]<=0:
                cnt_s.pop(s[i])
           
        
        return ans
                
