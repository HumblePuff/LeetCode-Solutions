class Solution:
    def dailyTemperatures(self, te: List[int]) -> List[int]:
    
        res = [0] * len(te)
        stack=[]
        for i, t in enumerate(te):
            while stack and t>stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t,i])
            
        return res