class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        mn = prices[0]
        for i in range(len(prices)):
            mx = max(mx, prices[i] - mn)
            mn = min(mn, prices[i])
        return mx