from queue import PriorityQueue
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9+7
        sum_speed=0
        a = sorted(zip(efficiency,speed),reverse=True)
        new_e,new_s = zip(*a)
        que = PriorityQueue()
        ans = 0 
        for a,b in zip(new_e,new_s):
            if que.qsize()>=k:
                sum_speed-=que.get()
            que.put(b)
            sum_speed+=b
            ans=max(ans, sum_speed*a)
        
        return ans%mod