class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        mn = prices[0]
        ans = 0
        mx_ind = 0
        mn_ind = 0
        for i in range(len(prices)):
            try:
                if mx < prices[i] - mn:
                    mx = prices[i] - mn
                    mx_ind = i
                if mn > prices[i]:
                    mn = prices[i]
                    mn_ind = i
                if (mx >= mn or prices[i] >= mn) and prices[i+1] < prices[i] and mx_ind != mn_ind:
                    ans += mx
                    mn = prices[i+1]
                    mx = 0
                    mn_ind, mx_ind = i+1, i+1
            except IndexError:
                ans += mx
        return ans