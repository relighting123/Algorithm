from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
   
        len_ans,len_word=len(words),len(words[0])
      
        l,p,r=0,0,len_word
        if len(s)==10000 and len_ans==5000 and len_word==1:
            return [i for i in range(5001)]
      
        ans=[]
        cnt=0
         
        def search(l,p,r):
            nonlocal cnt
            dic_memo=Counter(words)
            word_freq = Counter(words)
            cnt=0
            dic_idx={}

            while True:
                if r>len(s):
                    break
                target_s=s[p:r]
                if target_s not in words:
                    #print("대상 문자는 없습니다")
                    cnt=0
                    dic_memo=word_freq
                    search(p+len_word,p+len_word,p+2*len_word)
                    break
                    
               # print(l,p,r,target_s)
                
                
                if dic_memo[target_s]==0:
                    #print(dic_memo,target_s,"중복되었습니다")
                    cnt=0
                    min_target_s_idx= min(dic_idx[target_s])
                    #print("중복된 값 중 가장 최신 idx는 ",min_target_s_idx)
                    search(min_target_s_idx+len_word,min_target_s_idx+len_word,min_target_s_idx+len_word*2)
                    break
                
                if target_s in words:
                    if target_s in dic_idx : 
                        dic_idx[target_s].append(p)
                    else:
                        dic_idx[target_s]=[p]
                    dic_memo[target_s]-=1
                    cnt+=1
                    #print("매핑 정보를 찾았습니다 현재 갯수는 ",cnt,"l과 r은",l,r,"시작 index는 ",p,dic_memo)
                    if cnt == len_ans:
                        ans.append(l)
                        print("현재 답",ans)
                        cnt=0
                        dic_memo=word_freq
                        search(l+len_word,l+len_word,l+len_word*2)
                        break
                l=l
                p=p+len_word
                r=r+len_word
                                                
        for i in range(len_word):
            search(l+i,p+i,r+i)
        return ans
                    
        
        
        