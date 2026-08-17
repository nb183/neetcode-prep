# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([root])
        ans = []
        while queue:
            nodes_in_level = len(queue)
            current_nodes = []
            
            for _ in range(nodes_in_level):
                node = queue.popleft()
                if node:
                    current_nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if current_nodes:
                ans.append(current_nodes)
        return ans
