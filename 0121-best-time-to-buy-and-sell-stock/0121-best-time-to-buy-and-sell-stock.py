class Solution:
    def maxProfit(self, prices):

        buy, ans = float('inf'), 0
        for p in prices:
            buy, ans = min(buy, p), max(ans, p-buy)
        return ans