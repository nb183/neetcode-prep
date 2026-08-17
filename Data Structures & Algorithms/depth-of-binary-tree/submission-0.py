# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, maximum):
            if not node:
                return 0
            max1= dfs(node.left, maximum)
            max2= dfs(node.right, maximum)
            return maximum + max(max1, max2)
        ans = dfs(root, 1)
        return ans