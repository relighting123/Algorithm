
class Solution:
    def integerReplacement(self, n: int) -> int:
        ans=0
    
        while n!=1:
          #  print(n)
            if n%2==0:
                n=n//2
                ans=ans+1
            else :
                plus=list(bin(n+1))[::-1].index("1")
                minus=list(bin(n-1))[::-1].index("1")
                if n-1%n-2==0:
                    n=n-1
                    
                elif plus>minus:
                    n=n+1
                else :
                    n=n-1
            
                
                ans=ans+1
        return ans
        
    
            