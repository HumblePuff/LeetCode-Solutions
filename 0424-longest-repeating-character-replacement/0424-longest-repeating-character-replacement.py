from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):
        dic = defaultdict(int)
        start, end = 0, 0
        for end in range(1, len(s)+1):
            dic[s[end-1]] += 1
            if end-start-max(dic.values()) > k: 
                dic[s[start]] -= 1
                start += 1
        return end-start