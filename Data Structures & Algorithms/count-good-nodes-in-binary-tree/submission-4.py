# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Optimal - O(N) time, O(N) space
# We perform a dfs starting from the root node. We keep updating maximum variable which tracks 
# the maximum value seen in the path and compare each node to this maximum, and update the count

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maximum):
            ans = 0
            if not node:
                return 0

            if node.val >= maximum:
                maximum = node.val
                ans = 1
            
            ans += dfs(node.left, maximum)
            ans += dfs(node.right, maximum)
            return ans

        return dfs(root, -101)



   
            
