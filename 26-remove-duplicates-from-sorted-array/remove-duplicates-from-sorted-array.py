class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = []
        for ind in range(len(nums)-1):
            if nums[ind] == nums[ind+1]:
                continue
            ans.append(nums[ind])
        ans.append(nums[-1])
        nums[:] = ans
        return len(ans)
