class Solution(object):
    def productExceptSelf(self, n): 
        res=[1]*(len(n))
        prefix=1
        for i in range(len(n)):
            res[i]*=prefix
            prefix *= n[i]
        postfix=1
        for i in range(len(n)-1,-1,-1):
            res[i]*=postfix
            postfix *= n[i]
        return res