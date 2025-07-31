class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_window = sum(nums[:k])
        max_avg = sum_window
        for ind in range(k, len(nums)):
            sum_window -= nums[ind-k] 
            sum_window += nums[ind]
            max_avg = max(max_avg, sum_window)
        return max_avg/k
            