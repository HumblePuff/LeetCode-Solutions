class Solution:
    def isBalanced(self, root: TreeNode, h=1) -> bool:
        if not root: return h
        l = self.isBalanced(root.left, h+1)
        r = self.isBalanced(root.right, h+1)
        return abs(l-r) <= 1 and max(l, r)