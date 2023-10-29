class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def isAnagram(cnt_s,cnt_p):
            #조건에 대해 cnt_s==cnt_p로 하면 속도가 26.92%로 저조하여 개선
            for key,val in cnt_s.items():
                if key not in cnt_p:
                    return False
                else :
                    if val != cnt_p[key]:
                        return False
        cnt_p,len_p = Counter(p),len(p)
        cnt_s = Counter(s[0:len_p])
        ans=[]
        j=len_p-1
        for i in range(len(s)-len_p+1):
            ##Anagram 처리 가능시 인덱스 추가
            if cnt_s==cnt_p:
                ans.append(i)
            ## 후처리                   
            j+=1
            if j>=len(s):
                break
            cnt_s[s[j]]+=1       
            cnt_s[s[i]] -=1
            if cnt_s[s[i]]<=0:
                cnt_s.pop(s[i])
           
        
        return ans
                
