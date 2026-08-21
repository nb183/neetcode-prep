"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}

        def dfs(node):
            if node in mp:
                return mp[node]
            new_node = Node(node.val)
            mp[node] = new_node

            for neigh in node.neighbors:
                new_node.neighbors.append(dfs(neigh))

            return new_node
        
        return dfs(node) if node else None

        