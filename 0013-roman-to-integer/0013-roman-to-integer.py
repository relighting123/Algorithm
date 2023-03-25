class Solution(object):
    def romanToInt(self, s):
        
        dic = {'I' :1, 'V' :5, 'X':10,'L':50, 'C' :100, 'D':500,'M':1000}
        specialcase =['IV','IX','XL','XC','CD','CM']
        ans=0
        i=0
        while(i<len(s)):
            if len(s)>=2 and s[i:i+2] in specialcase :
                print(s[i:i+2])
                ans += dic[s[i+1]] -dic[s[i]]
                s=s[i+2:]
                continue
            one_s = s[i]
            ans += dic[one_s]
            s=s[i+1:]
                
        return ans
            
        
        