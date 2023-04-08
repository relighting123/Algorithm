class Solution(object):
    def minWindow(self, s, t):
            
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        answer=""
        start,end = 0,-1
        if(len(t)>len(s)) :
            return ""
        
        ##dict_t : number of unique Character ex) dict_s = {a:1,b:2} -> s문자열 내에 a는 1개, b는 2개 있다는 의미
        dict_t = collections.Counter(t)
        

        ##int_flag : 0인 경우 모든 문자를 찾은 상태로 정의. +인 경우 추가로 찾아야 하는 문자가 존재
        int_flag = sum(dict_t.values())
        
        while(end<len(s)-1):
            end+=1
            if s[end] in dict_t:
                dict_t[s[end]]-=1
                if dict_t[s[end]]>=0:
                    int_flag -=1
                
            while(int_flag <= 0 and start<len(s)):
                if ( int_flag <=0 and max(dict_t.values())<=0 and (len(s[start:end+1]) <len(answer) or answer=="")):
                    answer= s[start:end+1]
     
                if s[start] in dict_t:
                    dict_t[s[start]]+=1
                    if dict_t[s[start]]>0:
                        int_flag+=1
                start+=1
        
        return s[start:end+1] if int_flag ==0 else answer                
