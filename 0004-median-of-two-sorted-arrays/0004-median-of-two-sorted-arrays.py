class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        
        n3=n1+n2
        r=statistics.median(n3)
        return r
        