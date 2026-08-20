# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Solution -> O(N) time, O(N) space (can optimize the space to O(1) I think)
        # We can just do an inorder traversal of the BST, and put the elements in an array.
        # As inorder traversal gives the sorted list, we just get the kth element.

        arr = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]

        