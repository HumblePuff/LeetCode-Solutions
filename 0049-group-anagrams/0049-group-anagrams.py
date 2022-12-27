class Solution(object):
    def groupAnagrams(self, strs):

        anagrams = defaultdict(list)        
        for w in strs: anagrams[str(sorted(w))].append(w)        
        return anagrams.values()