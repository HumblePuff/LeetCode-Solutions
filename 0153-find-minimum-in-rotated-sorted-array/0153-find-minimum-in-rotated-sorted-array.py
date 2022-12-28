class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        try:
            res = min(nums)
        except ValueError:
            res = -1
        return res
        
