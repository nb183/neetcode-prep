class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = defaultdict(int)
        for t in tasks:
            mp[t] += 1

        sorted_tasks = sorted(mp.values(), reverse=True)
        max_task = sorted_tasks[0]

        max_task_count = 0

        for task in sorted_tasks:
            if task != max_task:
                break
            max_task_count += 1

        return max((max_task - 1) * (n + 1) + max_task_count, len(tasks))
