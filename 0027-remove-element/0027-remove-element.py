class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, 0
        while i < len(nums):
            if nums[i] != val:
                if nums[i] != '_': k += 1
                i += 1
            else:
                try:
                    nums.remove(val)
                    nums.append("_")
                except IndexError:
                    break  
        return k