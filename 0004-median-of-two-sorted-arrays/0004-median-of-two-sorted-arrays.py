class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        
        return statistics.median(n1+n2)
        
        