class Solution:
    def rightSideView(self, root):
            ans,nodes=[],[root]
            tmp=[]
            while root and nodes:
                ans.append(nodes[-1].val)
                nodes=[kid for 
                       node in nodes
                       for kid in (node.left,node.right) if kid]
            return ans
        
