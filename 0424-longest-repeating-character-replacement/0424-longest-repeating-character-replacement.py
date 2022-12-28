from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):
        dic = defaultdict(int)
        start = 0
        End = 0
        last_element=len(s)+1
        for end in range(1, last_element):
            dic[s[end-1]] += 1
            if end-start-max(dic.values()) > k:
                dic[s[start]] -= 1
                start += 1
        return end-start                            