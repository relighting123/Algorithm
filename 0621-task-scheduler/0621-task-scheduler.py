from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = defaultdict(int)
        for task in tasks:
            task_freq[task] += 1
        
        max_freq = 0
        num_max_freq = 0
        for freq in task_freq.values():
            if freq > max_freq:
                max_freq = freq
                num_max_freq = 1
            elif freq == max_freq:
                num_max_freq += 1
        
        idle_time = (n - num_max_freq + 1) * (max_freq - 1)
        remaining_tasks = len(tasks) - max_freq * num_max_freq
        
        return len(tasks) + max(0, idle_time - remaining_tasks)