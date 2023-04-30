class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # Calculate the least number of units of time needed to finish all tasks
        result = (max_freq - 1) * (n + 1) + max_count

        return max(result, len(tasks))