
from collections import deque
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        minPoint = max(0, startPos - k)  
        maxPoint = startPos + k          
        fruits_dict = {item[0]: item[1] for item in fruits}
        queue = deque()
        fruits_queue = deque()
        for item in fruits:
            if startPos+k>=item[0] and startPos<=item[0]:
                queue.append(item)
            elif startPos > item[0] and startPos-k<=item[0]:
                fruits_queue.append(item)
        
        a,b= startPos,startPos+k
        
        ans =  sum(sublist[1] for sublist in queue)
        t_ans=ans
        
        while a>=startPos-k and fruits_queue:
            next_fruitsloc = fruits_queue[-1][0]
 
            a= next_fruitsloc
            temp_b=b
            if startPos<=a or a+k<=startPos:
                b=a+k
            else:
                b = max(startPos + k - 2 * abs(startPos - a) ,startPos + (k-startPos+a)//2)
            while temp_b >b and queue and queue[-1][0]>b and temp_b >= queue[-1][0]:
                t_ans -= queue[-1][1]
                queue.pop()
                temp_b-=1
            t_ans=t_ans+fruits_queue[-1][1]
            fruits_queue.pop()

            print(a,b,t_ans)
            ans=max(ans,t_ans)
        return ans
                                      
            
        
            
            
        