# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, val):
            if not node:
                return val

            val += 1

            return max(dfs(node.left, val), dfs(node.right, val))

        return dfs(root, 0)
        