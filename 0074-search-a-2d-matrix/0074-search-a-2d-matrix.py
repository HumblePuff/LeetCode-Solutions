from itertools import chain

class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        flatten_list = list(chain.from_iterable(m))
        if target in flatten_list:
            return True
        else:
            return False
    