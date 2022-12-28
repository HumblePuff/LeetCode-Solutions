class Solution:
    def maxProfit(self, prices):

        buy = float('inf')
        ans = 0
        for p in prices:
            buy = min(buy, p)
            ans = max(ans, p-buy)
        return ans