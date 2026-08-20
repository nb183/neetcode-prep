# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        queue = deque([(root, 0)])
        prev_level = prev_val = -1

        while queue:
            node, level = queue.popleft()
            if prev_val != -1 and level != prev_level:
                ans.append((prev_val))
            print(node.val, level, prev_level)
            prev_level = level
            prev_val = node.val
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        ans.append(prev_val)

        return ans







        