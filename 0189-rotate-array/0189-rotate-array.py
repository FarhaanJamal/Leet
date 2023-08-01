class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k < len(nums):
            nums[:] = nums[-k:] + nums[:-k]
        else:
            for _ in range(k):
                cur_val = nums[-1]
                for i in range(len(nums)):
                    nxt_val = nums[i]
                    nums[i] = cur_val
                    cur_val = nxt_val