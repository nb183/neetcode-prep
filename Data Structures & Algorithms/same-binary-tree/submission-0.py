# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root):
            queue = []
            nodes = []
            if not root:
                return nodes
            queue = [root]
            while queue:
                top = queue.pop(0)
                if top:
                    nodes.append(top.val)
                    queue.append(top.left)
                    queue.append(top.right)
                else:
                    nodes.append(10001)
            return nodes
        return bfs(p) == bfs(q)