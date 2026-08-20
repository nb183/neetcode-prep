# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = []

        def dfs(node, maximum):
            if not node:
                return None

            if node.val >= maximum:
                maximum = node.val
                ans.append(node.val)
            
            dfs(node.left, maximum)
            dfs(node.right, maximum)

        dfs(root, -101)

        return len(ans)


   
            
