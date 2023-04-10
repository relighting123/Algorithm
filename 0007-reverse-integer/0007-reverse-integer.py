class Solution(object):
    def reverse(self, x):
        if x==0:
            return x
        signed=1
        max_val= 0
        if x<0 : 
            x=x*(-1)
            signed=-1
        
        len_num =int(math.log10(x))
        ans,len_ans = 0,0
        val = x// 10**(len_num)
        i,temp=0,0
        while len_ans<=len_num:
            mok= x//10**(len_num-i) 
            x-=mok*10**(len_num-i)  
            ans+=mok*10**(i)  
            len_ans =int(math.log10(ans))
            if len_num==i and mok ==0:
                return signed*ans
            
            if len_ans==len_num : 
                ans = signed * ans
                if -2**(31)<=  ans <2**(31):
                    return ans
                else:
                    return 0
            i+=1
        
        return ans