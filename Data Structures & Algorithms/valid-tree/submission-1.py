class UnionFind:
    def __init__(self, n): # n represents the number of nodes in the graph
        self.par = {} # parent of a node
        self.rank = {} # rank/height of node

        for i in range(0, n):
            self.par[i] = i # initally each node is its own parent
            self.rank[i] = 0 # assume 0 rank for single nodes

    def find(self, n):
        # traverse the parent of a node unit it is its own parent

        p = self.par[n]

        while p != self.par[p]:
            # path compression optimisation
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        # union by rank
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] > self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for u, v in edges:
            if not uf.union(u, v):
                return False
        
        count = 0

        max_rank = max(uf.rank.values())
        count = list(uf.rank.values()).count(max_rank)
 
        if count > 1:
            return False

        return True
        