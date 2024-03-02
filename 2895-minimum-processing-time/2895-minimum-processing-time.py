class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        n_tasks = len(tasks)
        n_procs = len(processorTime)
        
        subarr = [tasks[i:i+4] for i in range(0, n_tasks, 4)]
        
        i = 0
        min_time = float('-inf')
        for arr in subarr:
            
            for j, task in enumerate(arr):
                arr[j] = task + processorTime[i]
                
            min_time = max(min_time, max(arr))
            i += 1
            
        return min_time
            