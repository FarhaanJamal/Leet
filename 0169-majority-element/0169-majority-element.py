class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = []
        ln = len(nums)/2
        n = 0
        while n < ln*2:
            if nums[n] not in seen and nums.count(nums[n]) >= ln:
                return nums[n]
            else:
                seen.append(nums[n])
            n += 1