class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for pre in prerequisites:
            graph[pre[0]].append(pre[1])

        visit = set()
        visited = set()
        order = []

        def dfs(node):
            if node in visit:
                return False
            if node in visited:
                return True
            visit.add(node)
   
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            visit.remove(node)
            order.append(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order
