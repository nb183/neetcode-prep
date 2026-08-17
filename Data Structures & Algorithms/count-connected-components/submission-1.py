class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        numConnected = n
        parent = [i for i in range(n)]
        rank = [1] * (n)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node 

        def union(node1, node2):
            node1 = find(node1)
            node2 = find(node2)
            if parent[node1] == parent[node2]:
                return False

            if rank[node1] <= rank[node2]:
                parent[node2] = node1
                rank[node1] += rank[node2]
            else:
                parent[node1] = node2
                rank[node2] += rank[node1]
            return True

        for edge in edges:
            numConnected -= union(edge[0], edge[1])

        return numConnected
