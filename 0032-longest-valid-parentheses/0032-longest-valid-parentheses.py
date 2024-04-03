class Solution:
    def longestValidParentheses(self, s: str) -> int:
        que = deque([])
        maxans,ans=0,0 
        if len(s)==0:
            return 0
        s="s"+s+"e"
        que.append((s[0],0))
        for i in range(1,len(s)):
            char = s[i]
            que.append((char,i))
            if len(que)>=2:
                a=que.pop()
                b=que.pop()
                if b[0]+a[0]!='()':
                    que.append(b)
                    que.append(a)
                continue
        lastidx=len(s)-1
        if len(que)==0:
            return len(s)
    
        while que:
            idx=que.pop()
            val=lastidx-idx[1]
            ans=max(ans,val)
            lastidx=idx[1]
        
        return ans-1
            
            
      
    
    
    

            
                