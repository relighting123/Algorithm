class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = [(-tasks.count(task), task) for task in set(tasks)]
        heapq.heapify(task_freq)
        
        intervals = 0
        while task_freq:
            i, temp = 0, []
            while i <= n:
                intervals += 1
                if task_freq:
                    freq, task = heapq.heappop(task_freq)
                    if freq < -1:
                        temp.append((freq+1, task))
                if not task_freq and not temp:
                    break
                i += 1
            for freq, task in temp:
                heapq.heappush(task_freq, (freq, task))
        
        return intervals