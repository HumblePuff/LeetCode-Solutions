from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len: int = 0

        pos = defaultdict(int)
        
        start: int = 0
        
        for end, ch in enumerate(s):
            start = max(start, pos[ch])
            max_len = max(max_len, end-start+1)
            pos[ch] = end + 1
                
        return max_len