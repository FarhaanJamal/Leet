class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        j = 0
        while i < len(nums):
            if i + nums[i] > j:
                j = i + nums[i]
            if i == j:
                break
            i += 1
        return j >= len(nums)-1