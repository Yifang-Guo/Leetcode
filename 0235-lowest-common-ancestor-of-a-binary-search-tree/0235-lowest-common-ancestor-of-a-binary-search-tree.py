# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == root.val or q.val == root.val:
            return root

        if self.onTheSameSide(root, p, q):
            if max(p.val, q.val) < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            elif min(p.val, q.val) > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def onTheSameSide(self, root, p, q):
        if p.val < root.val < q.val:
            return False
        elif q.val < root.val < p.val:
            return False
        else:
            return True
        