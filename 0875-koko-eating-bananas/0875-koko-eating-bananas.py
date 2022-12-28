class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # in order to eat all bananas, koko has to eat at least one every hour
        leastBananaToEat = 1
        # koko can only eat from one pile at a time, so she cannot eat more than the amount of bananas in the largest pile
        mostBananaToEat = max(piles)
        
        while leastBananaToEat < mostBananaToEat:
            bestRate = (leastBananaToEat + mostBananaToEat) // 2
            
            # find the time it takes for koko to finish all bananas if she eats 'bestRate' amount of bananas per hour
            totalHours = 0
            for pile in piles:
                # koko continues to eat from the same pile until she finishes it
                totalHours += math.ceil(pile / bestRate)
                    
            if totalHours > h:
                # it's impossible to eat all bananas within the hour constraint 
                # need to look for a valid rate -- increase the rate of banana eating in the next iteration
                leastBananaToEat = bestRate + 1
            else:
                # it's possible to eat all bananas within the hour constraint 
                # try to see if koko can eat slower -- decreaase the rate of banana eating in the next iteration
                mostBananaToEat = bestRate 
        return leastBananaToEat