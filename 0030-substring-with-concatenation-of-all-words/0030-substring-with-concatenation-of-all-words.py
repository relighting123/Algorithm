from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
   
       
         
        def search(l,p,r,dic_memo,dic_idx,cnt):

            
            word_freq = Counter(words)

            while True:
                if r>len(s):
                    break
                target_s=s[p:r]
                if target_s not in words:
                    #print(l,p,r,"대상 문자는 없습니다")
                    cnt=0
                    dic_memo=word_freq
                    dic_idx={}
                    search(p+len_word,p+len_word,p+2*len_word,dic_memo,dic_idx,cnt)
                    break
                    
                #print(l,p,r,target_s,dic_idx)
                
                
                if dic_memo[target_s]==0:
                    #print(dic_memo,dic_idx,target_s,"중복되었습니다")

                   
                    min_target_s_idx= min(dic_idx[target_s])
                    #[l,min_target_s_idx] 대상 글자에 대해서 count +1 처리하여 다시 선택 가능하도록 적용
                    #print("회복 대상",l,min_target_s_idx,"현재 cnt",cnt)
                    for i in range(l,min_target_s_idx+1,len_word):
                        print(i,s[i:i+len_word],"회복합니다.")
                        dic_memo[s[i:i+len_word]]+=1
                        dic_idx[s[i:i+len_word]].pop(0)
                        cnt-=1
                    
                    #print("중복된 값 중 가장 최신 idx는 ",min_target_s_idx,p,dic_memo,"계산후 cnt",cnt)
                    search(min_target_s_idx+len_word,p,p+len_word,dic_memo,dic_idx,cnt)
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
                        #print("현재 답",ans)
                        dic_memo[s[l:l+len_word]]+=1
                        dic_idx[s[l:l+len_word]].pop(0)
                        cnt-=1
                        search(l+len_word,p+len_word,p+len_word*2,dic_memo,dic_idx,cnt)
                        break
                l=l
                p=p+len_word
                r=r+len_word
                
                
                
        len_ans,len_word=len(words),len(words[0])        
        ans=[]
        
        for i in range(len_word):
            #이 2개 라인이 없으면 이전 결과를 활용하는 것으로 보임 이유는?
            
            l,p,r=0,0,len_word  
            dic_memo=Counter(words)
            dic_idx={}            
            cnt=0
            search(l+i,p+i,r+i,dic_memo,dic_idx,cnt)
        return ans
                    
        
        
        