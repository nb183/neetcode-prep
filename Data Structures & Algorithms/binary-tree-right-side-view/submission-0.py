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
        while queue:
            node, level = queue.popleft()
            ans.append((node.val, level))
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        result = []

        for i, item in enumerate(ans):
            if i == len(ans) - 1 or item[1] != ans[i+1][1]:
                result.append(item[0])

        return result







        