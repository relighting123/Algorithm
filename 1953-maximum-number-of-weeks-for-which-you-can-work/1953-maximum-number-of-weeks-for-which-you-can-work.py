class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        task_list = sum(milestones)
        max_task_cnt = max(milestones)
        num_distinct_cnt = sum(1 for i in milestones if i==max_task_cnt)
        if num_distinct_cnt>=2:
            idle=0
        else:
            idle = (max_task_cnt-1)
        remain_task=task_list-num_distinct_cnt*max_task_cnt
        if idle<remain_task:
            return max(idle,remain_task)+num_distinct_cnt*max_task_cnt
        else:
            return max(idle,remain_task)+num_distinct_cnt*max_task_cnt - 2*(idle-remain_task)