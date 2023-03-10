class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return 1
        l = self.isBalanced(root.left)
        if not l: return False
        r = self.isBalanced(root.right)
        if not r: return False
        if abs(l-r) <=1 :
            return 1+ max(l,r)
        else:
            return False