# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Solution: O(N) time and O(N) space
        # First we wanna store the index of each element of the inorder array,as that is very important
        # to determine the position of root and number of elements in the left and right subtree
        # preoder traversal traverses the root first so the first value in the preorer is always the root
        # inorder traverses the root at the middle, so the root divides the inorder array to two halves
        # We take these and first take the first element of the preorder array as root and then get its index
        # in the inorder array. The elements before that index will be left subtree and after right subtree
        # We can do this recursively to build the tree. In our solution we use two pointers each for the 
        # preorder and inorder to track the number of elements in left and right subtree and the actual elements
 
        mp = {val: i for i, val in enumerate(inorder)}
        n = len(inorder)

        def dfs(p_l, p_r, i_l, i_r):
            if p_l > p_r or i_l > i_r:
                return None

            root = TreeNode(preorder[p_l])
            pivot = mp[root.val]

            left_size = pivot - i_l

            root.left = dfs(p_l + 1, p_l + left_size, i_l, pivot - 1)
            root.right = dfs(p_l + left_size + 1, p_r, pivot + 1, i_r)

            return root

        return dfs(0, n - 1, 0, n - 1)

        