class Solution:
    def rightSideView(self, root):
            ans,nodes=[],[root]
            tmp=[]
            while root and nodes:
                ans.append(nodes[-1].val)
                tmp=[]
                for node in nodes:
                    for kid in (node.left,node.right):
                        if kid:
                            tmp.append(kid)
                nodes=tmp
            return ans
        

                
            