class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pre, post = 1, 1
        for i in range(len(nums)):
            ans[i] *= pre
            ans[-1-i] *= post
            pre = pre*nums[i]
            post = post*nums[-1-i]
        return ans