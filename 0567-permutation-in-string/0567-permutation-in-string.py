class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
               
        s1Counter = {}
        s2Counter = {}
        
        for char in s1:
            if char not in s1Counter:
                s1Counter[char] = 0
            s1Counter[char] += 1
        
        start = 0
        
        for end, char in enumerate(s2):
            

            if char not in s2Counter:
                s2Counter[char] = 0
            s2Counter[char] += 1
            

            windowSize = end - start + 1
            if windowSize == len(s1):
                
                if s1Counter == s2Counter:
                    return True

                if s2Counter[s2[start]] == 1:
                    del s2Counter[s2[start]]
                else:
                    s2Counter[s2[start]] -= 1
                    
                start += 1
				
        return False