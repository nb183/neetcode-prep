class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for item in prerequisites:
            graph[item[0]].append(item[1])

        def dfs(node):
            if node in visit:
                return False
            if graph[node] == []:
                return True
            visit.add(node)
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            visit.remove(node)
            graph[node] = []
            return True
            
        visit = set()

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True

    

        