class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        l = self.isBalanced(root.left)
        if not l: return
        r = self.isBalanced(root.right)
        if not r: return
        return abs(r - l) <= 1 and 1 + max(l, r)