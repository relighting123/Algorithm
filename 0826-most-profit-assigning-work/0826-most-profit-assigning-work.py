class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(profit)
        mapper = [(difficulty[i],profit[i]) for i in range(n)]
        mapper.sort(key = lambda x:x[0])
        worker.sort()
        
        cur_max=0
        ans=0
        ptr_job=0
        ptr_lastjob=0
        chk = 0
       # print('기본 정보',mapper,worker)
        while chk < len(worker) :
            #print(ptr_job,chk)
            for ptr_job in range(ptr_lastjob,n):
                worker_ability=worker[chk]
                job_hard = mapper[ptr_job][0]
                job_profit=mapper[ptr_job][1]
                if worker_ability<job_hard :
                    break
                if worker_ability>=job_hard :
                    cur_max = max(cur_max,mapper[ptr_job][1])
                    
            ans+=cur_max
            chk+=1
            ptr_lastjob=ptr_job
        #print(ans)
        return ans
        
            
            
            
            
        
        
        
        
        