from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_list = Counter(tasks).values()
        max_task_cnt = max(task_list)
        num_distinctmax_cnt = sum(1 for i in task_list if i==max_task_cnt)
        idle = (n-num_distinctmax_cnt+1)*(max_task_cnt-1)
        remain_task= sum(task_list)-max_task_cnt*num_distinctmax_cnt
        
        if idle>remain_task:
            return idle+max_task_cnt*num_distinctmax_cnt
        else:
            return  remain_task+max_task_cnt*num_distinctmax_cnt
            
           