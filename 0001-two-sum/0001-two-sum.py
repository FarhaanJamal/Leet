class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        dict = {}
        for ind, val in enumerate(nums):
            rem = target - val
            if rem in dict:
                ans = [ind, dict[rem]]
                break
            else:
                dict[val] = ind
        return ans