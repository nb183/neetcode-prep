# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Bruteforce -> O(N) TC, O(N) SC
# We do a dfs keeping track of the nodes and levels. When we pop out 
# an element from the queue, if it is not euql to level of the previous 
# node, that means that the last node was the right most node in the 
# previous level. So, we will add the node the answer.

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
            prev_level, prev_val = level, node.val
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        ans.append(prev_val)

        return ans







        